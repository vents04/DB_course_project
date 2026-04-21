# Задача 3: Технологична архитектура — Дигитален процес по жалби

Този документ описва инфраструктурната архитектура на услугата „Дигитален процес по жалби“ в UniCredit Bulbank. Източникът на истината е диаграмата [`architecture.drawio`](architecture.drawio), разработена в [diagrams.net](https://app.diagrams.net). Архитектурата стъпва на стандартния банков модел за сегментация: периметрена защитна стена, DMZ, вътрешни защитни стени и сегментирана вътрешна мрежа (App + DB).

## Как се чете диаграмата

Диаграмата се чете **отгоре надолу**, по ред на **нарастващо доверие** спрямо банковата инфраструктура:

1. Клиентски устройства + Интернет + външни push услуги
2. Периметрена защитна стена (CheckPoint)
3. DMZ NW segment — reverse proxy + LB, NGINX/WAF двойка, egress web proxy
4. Вътрешна защитна стена между DMZ и Datacenter
5. Datacenter → App NW Segment — Flex Cube (CBS), Internal LB, backend HA двойка, AI Copilot
6. Вътрешна защитна стена между App и DB сегменти
7. Datacenter → DB NW Segment — ComplaintsDB (PostgreSQL), ObjectStore (MinIO) със съхранение за прикачени файлове и одитни записи

## Клиентска страна (публичен Интернет)

**Клиент** — автентикиран потребител на банката; самоличността е доказана чрез логина (биометрия / ПИН), без нужда от КЕП.

**BBM Mobile App** — основният канал за подаване на жалби. Използва **HTTPS 443** към публичния endpoint `bbm.unicredit.bg`.

**Push Notification Services** — външен партньор (Firebase / FCM, APNs за iOS). Push нотификациите се задействат **от банковия сървър**, не директно от клиентското приложение. Изходящият трафик към push доставчиците минава през dedicated Web Proxy в DMZ с allowlist.

## Периметрена защитна стена

**CheckPoint FW** — публичен IP `82.123.300.31`, NAT към вътрешен `192.168.10.4`. Разрешава само входящ **TCP 443 (HTTPS)** от Интернет към DMZ reverse proxy. Трафикът се терминира на reverse proxy, не директно на вътрешни сървъри.

## DMZ NW Segment

**Reverse Proxy + LB** (`192.168.10.4/24`) — публичен слушател 443/tcp HTTPS. Терминира TLS, балансира към двете WAF проксита.

**BBMComplProxy1 / BBMComplProxy2** (`192.168.20.4` и `192.168.20.5`) — HA двойка на **NGINX + ModSecurity** върху **RHEL 9**, 4 CPU / 16 GB RAM всяка. Функции: правила срещу OWASP Top 10, rate limiting, маршрутизация към вътрешния сегмент. **WAF двойката играе ролята на входна точка към API** — отделен Spring Cloud Gateway не е необходим в този мащаб.

**Web Proxy** (`192.168.11.6/24`) — изходящ allowlist-прокси за трафика от backend-ите към външни партньори (push services). Изолира изходящите връзки от входящия път.

## Вътрешна защитна стена (DMZ → Datacenter)

Сегментирани правила; App NW Segment приема трафик **само от DMZ прокситата на порт 443**, не от произволни клиенти.

## Datacenter → App NW Segment

### Flex Cube (Core Banking System)

- **Адрес:** `192.168.30.10/24`
- **Стек:** Oracle Flex Cube върху WebLogic 12, JRE 11, RHEL 9
- **Капацитет:** 8 CPU / 64 GB RAM
- **Роля:** Система на записа за клиенти, сметки, карти и транзакции. Complaints бекендите я четат за контекст и я обновяват при монетарни действия (компенсации, връщане на такси) през REST/JSON + mTLS на порт 443.

Flex Cube е *наследена* система — Complaints услугата не я замества, а я интегрира.

### Internal LB

Балансира вътрешния трафик между DMZ прокситата и backend HA двойката (порт 443).

### BBMPComplBackEnd1 / BBMPComplBackEnd2

- **Адреси:** `192.168.30.4` и `192.168.30.5` (HA двойка)
- **Стек:** **Spring Boot** върху **JBoss EAP 8**, **JRE 21**, RHEL 9
- **Капацитет:** 6 CPU / 32 GB RAM всеки
- **Роля:** Complaints Orchestrator — реализира процеса: валидации, състояния (чернова → регистрирана → разследване → решение → затворена), маршрутизация към специалист, интеграция с Flex Cube и AI Copilot, управление на одитни записи.

### AI Copilot

- **Адрес:** `192.168.30.20/24`
- **Стек:** Python 3.12 + FastAPI, self-hosted, RHEL 9
- **Капацитет:** 4 CPU / 16 GB RAM
- **Функции:** асемблира контекст (транзакции, предходни случаи, подобни решения) и изготвя чернова на отговор за специалиста.
- **Регулаторна роля:** AI **не** взема решения и не изпълнява автономно монетарни или регулирани действия (съгласно EBA/GL/2015/18) — специалистът винаги приема или коригира предложението преди то да се изпрати към клиента. Никакви клиентски данни не напускат банковата мрежа.

## Вътрешна защитна стена (App → DB)

Втори сегментационен граничен слой. App сегментът достъпва DB сегмента само на договорени портове (5432 за PostgreSQL, 9000 за S3), и само от конкретните backend адреси.

## Datacenter → DB NW Segment

| Компонент | Адрес | Порт | Роля |
|---|---|---|---|
| **ComplaintsDB** | `192.168.31.4/24` | 5432/tcp (TLS) | PostgreSQL 16 на RHEL 9, 8 CPU / 32 GB RAM. Система на записа за жалбите: статуси, референтни номера, история, решения. |
| **ObjectStore** | `192.168.31.5/24` | HTTPS 9000 (S3 API) | MinIO на RHEL 9, 4 CPU / 16 GB RAM. Съхранява прикачени файлове (сканирани документи, скрийншоти) **и одитни записи** в append-only bucket-и с object-lock политика. |

Само приложният слой достига тези услуги; **няма директен Интернет достъп** и никакъв входящ път от Клиент към DB сегмента.

## Таблица „стрелка → протокол"

| От | До | Протокол | Бележка |
|---|---|---|---|
| BBM Mobile → Internet → Perimeter FW | HTTPS 443 | TLS 1.2+ |
| Perimeter FW → Reverse Proxy + LB | HTTPS 443 | NAT terminate |
| Reverse Proxy → BBMComplProxy1/2 | HTTPS 443 | internal |
| BBMComplProxy1/2 → Internal FW → Internal LB | HTTPS 443 | WAF-filtered |
| Internal LB → BBMPComplBackEnd1/2 | HTTPS 443 | balanced |
| Backend ↔ Flex Cube (CBS) | REST/JSON 443 **mTLS** | двупосочна (четене на контекст + изпълнение на компенсации) |
| Backend → AI Copilot | REST/JSON 443 | internal |
| Backend → Internal FW → ComplaintsDB | 5432 (TLS) | PostgreSQL |
| Backend → Internal FW → ObjectStore | 9000 (S3 HTTPS) | attachments + audit |
| Backend → Web Proxy → Push Services | HTTPS 443 | egress allowlist |

## Регулаторно позициониране

- **ЗПУПС чл. 174** — срокът за отговор (15 раб. дни, 35 при изключения) се следи от Complaints Orchestrator чрез SLA мониторинг върху ComplaintsDB.
- **EBA/GL/2015/18** — append-only съхранение в ObjectStore с object-lock покрива изискванията за регистрация и проследимост на всяка жалба.
- **GDPR чл. 5** — PII не напуска банковата мрежа; AI Copilot е self-hosted; всички канали са TLS 1.2+; достъпът до DB сегмента е ограничен до конкретни backend адреси.

## Легенда на фигурите

| Фигура | Значение |
|---|---|
| Android телефон | Клиентско устройство |
| Облак (син) | Публичен Интернет |
| Облак (оранжев) | Външен партньор (push) |
| Щит (червен) | Защитна стена |
| Router / switch | Reverse proxy / Internal LB |
| Standard host | Приложен / WAF / AI / CBS сървър |
| FC storage | База данни / object store |
| Пунктиран контейнер | Мрежов сегмент (DMZ / App / DB) |

## Как да отворите диаграмата

- [diagrams.net (app.diagrams.net)](https://app.diagrams.net/) — File → Open From → Device → изберете `architecture.drawio`
- VS Code с Draw.io Integration extension
- Desktop drawio приложение
