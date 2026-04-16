# Задача 3: Технологична архитектура — Дигитално управление на жалби

## Файлове в тази директория

| Файл | Тип | Описание |
|---|---|---|
| `technology_architecture.drawio` | draw.io XML | Единствената архитектурна диаграма — мрежова сегментация, сървъри с ОС, приложни сървъри, бази данни, външни услуги, firewall-и и комуникационни протоколи |
| `architecture.md` | Markdown | Този файл — метаданни и описание на диаграмата |

## Как да отворите диаграмата

Диаграмата е в `draw.io` формат (`.drawio`) — стандартен XML, който може да бъде зареден в:

- **[app.diagrams.net](https://app.diagrams.net/)** — **препоръчан**, безплатен онлайн редактор. Меню → File → Open from → Device → избор на `.drawio` файла. Без регистрация.
- **draw.io Desktop** — безплатно приложение за Windows / macOS / Linux
- **VS Code с „Draw.io Integration" extension** — за редактиране в IDE

## Какво покрива диаграмата (според изискванията на задачата)

| Изискване | Решение в диаграмата |
|---|---|
| a) Сървъри с ОС и приложни сървъри | Всеки компонент има OS (RHEL 9 / Ubuntu 22.04 / Windows Server 2022) и приложен сървър, където е приложимо (Tomcat 10, JBoss EAP 7.4, IIS 10, NGINX) |
| b) Мрежова сегментация с защити | 7 различни мрежови зони, разделени с 3 firewall-а (perimeter, internal, egress), WAF, Reverse Proxy, API Gateway |
| c) Технологии, протоколи, портове | Всеки компонент и всяка връзка имат изписани технологии, протоколи и портове |
| d) Връзки между приложенията | 37 стрелки между компонентите, всяка с протокол и порт |

---

## 1. Обхват на проекта

Диаграмата представя целевата технологична архитектура за реализация на **процеса по дигитално управление на жалби**, описан в Задача 1 (research) и Задача 2 (BPM). Тя включва:

- **Съществуващи системи** (не се променят от проекта) — BBO_BE, CORE_BANKING, CORE_ACC, CARD_SYSTEM, CRM
- **Нови компоненти за процеса по жалби** (разработка в този проект) — AI_CHATBOT, NLP_ENGINE, CMS, AI_COPILOT, NOTIF_SERVICE, AUDIT_LOG, Specialist Workbench, Analytics
- **Инфраструктура** — Firewall-и, WAF, Load Balancer, API Gateway, Identity Provider, бази данни, message bus, monitoring

Постулат (от заданието): банката вече разполага с онлайн канали — те не са предмет на разработка, а само се интегрират.

---

## 2. Мрежови зони

Архитектурата е разделена на **7 логически зони** (swim lanes в диаграмата), с мрежова сегментация през firewall-и:

### 2.1 Клиент (публичен Интернет)
Мобилни устройства (iOS/Android с Bulbank Mobile), уеб браузъри (Bulbank Online), email клиенти (за получаване на нотификации), push получаване (APNS/FCM).

### 2.2 DMZ (Demilitarized Zone)
Първа линия на защита. Всичко публично достъпно е тук:
- **WAF** (Web Application Firewall) — ModSecurity на RHEL 9, филтрира OWASP top-10 атаки
- **Load Balancer** — F5 BIG-IP или HAProxy, терминира TLS 1.3, разпределя трафика
- **Reverse Proxy** — NGINX 1.25 на RHEL 9, каши се, routes заявки
- **API Gateway** — Kong 3.x на Ubuntu 22.04, автентикация (OAuth2/JWT), rate limiting
- **Identity Provider** — Keycloak или UniCredit корпоративен SSO, Tomcat 10

Firewall-и: **Perimeter Firewall** (Palo Alto / Fortinet, L3/L4) отпред, **Internal Firewall** (L7 deep packet inspection) отзад.

### 2.3 Digital Channels Zone (съществуващи)
- **BBO_BE** — Булбанк Онлайн Backend, Spring Boot 3 на Java 21, Tomcat 10, RHEL 9
- **BBM Mobile Backend API** — Spring Boot 3, Tomcat 10, RHEL 9
- **Session / Auth Service** — Spring Boot, Tomcat 10, RHEL 9, използва Redis за сесии

### 2.4 Complaint Services Zone (НОВО)
Нова микросервизна зона за процеса по жалби. Цялата зона работи на **Kubernetes 1.29 (OpenShift 4.14)** с Istio service mesh за mTLS между услугите:

| Услуга | Технология | OS на контейнера | Порт |
|---|---|---|---|
| AI_CHATBOT | Python 3.12, FastAPI | RHEL UBI 9 | 8443 (REST), 8444 (WebSocket) |
| NLP_ENGINE | Python 3.12, PyTorch / ONNX, GPU (NVIDIA A10) | RHEL UBI 9 | 50051 (gRPC) |
| CMS (Complaint Mgmt System) | Spring Boot 3, Java 21, Tomcat 10, Camunda Zeebe | RHEL 9 | 8443 (REST mTLS) |
| AI_COPILOT | Python 3.12, FastAPI | RHEL UBI 9 | 8443 (REST mTLS) |
| NOTIF_SERVICE | Node.js 20, Express | Ubuntu 22.04 LTS | 8443 (REST mTLS) |
| AUDIT_LOG Service | Go 1.22 (append-only) | Alpine Linux | 8443 (REST mTLS) |
| Specialist Workbench | React 18, NGINX pod | Alpine Linux | 443 mTLS |
| Analytics / Trend Engine | Python, Airflow 2.x | RHEL UBI 9 | Kafka consumer |

### 2.5 Core Banking Zone (съществуващи)
Legacy Java EE системи, интегрират се, но не се променят:
- **CORE_BANKING** — Java EE 8 на JBoss EAP 7.4, RHEL 9
- **CORE_ACC** (Модул Сметки) — вграден в CORE_BANKING JBoss, RHEL 9
- **CARD_SYSTEM** (домейн) — .NET 8 на IIS 10, Windows Server 2022
- **CRM** (домейн) — Microsoft Dynamics 365 on-prem, IIS + SQL Server, Windows Server 2022
- **Integration Bus / ESB** — IBM MQ 9.3 на RHEL 9 за legacy адаптери

### 2.6 Database Zone
Изолирана зона — достъпна само по JDBC от приложните зони, не директно отвън:

| База | Употреба | OS | Порт |
|---|---|---|---|
| Oracle 19c Enterprise | Core Banking DB, Data Guard DR | RHEL 9 | 1521 (JDBC TLS) |
| PostgreSQL 15 | CMS DB (жалби, workflow state) | Ubuntu 22.04 LTS | 5432 (JDBC TLS) |
| PostgreSQL 15 | AUDIT_LOG DB — WORM, 7г retention, tamper-evident hash chain | Ubuntu 22.04 LTS | 5432 (mTLS) |
| Redis 7.2 | Сесии + кеш, Sentinel HA | RHEL 9 | 6379 (TLS) |
| MinIO Object Store | Прикачени файлове към жалби, AES-256 at rest | Ubuntu 22.04 LTS | 9000 (HTTPS S3 API) |
| Elasticsearch 8 | Търсене + analytics, 3-node cluster | Ubuntu 22.04 LTS | 9200 (HTTPS) |
| SQL Server 2022 | CRM + CARD_SYSTEM | Windows Server 2022 | 1433 (TDS TLS) |

### 2.7 External Services (през Egress Firewall)
Ограничен whitelist от SaaS и външни доставчици:

| Услуга | Достъп | Порт |
|---|---|---|
| SMTP Relay (Postfix / SendGrid) | Изходящ email до клиенти | 587 (STARTTLS) |
| Firebase Cloud Messaging (FCM) | Android push | 443 (HTTPS) |
| Apple Push Notification Service (APNS) | iOS push | 443 (HTTPS/2) |
| LLM API (Claude / Azure OpenAI / UniCredit AI) | Генеративни отговори | 443 private VPC peering |
| Външни регулатори (БНБ, КЗП, ПКПС, FIN-NET) | За ескалация | 443 / secure file transfer |
| КЕП валидация (B-Trust / InfoNotary) | За канали извън приложението | 443 |

### 2.8 Message Bus
**Apache Kafka 3.7** cluster (3 брокера, RHEL 9) — TLS порт **9093**, SASL/SCRAM автентикация. Всички събития за жалби (създаване, статус, нотификации) минават през Kafka за decoupling между услугите.

### 2.9 Management / Monitoring (изолирана, bastion-only)
- **ELK Stack** (Elasticsearch + Logstash + Kibana) — централизирани логове
- **Prometheus + Grafana** — метрики и дашбордове
- **HashiCorp Vault** — secrets management, TLS сертификати
- **GitLab + Argo CD** — CI/CD
- **Bastion Host** — SSH jump server за административен достъп
- **SIEM** (Splunk / Wazuh) — security events, integration с одит лога

---

## 3. Ключови комуникационни връзки

### 3.1 Входящ трафик (Client → Internal)
1. Клиент → Интернет: **HTTPS 443, TLS 1.3**
2. Интернет → WAF → Load Balancer → Reverse Proxy → API Gateway: през DMZ, с терминиране на TLS и mTLS re-encryption
3. API Gateway → BBO_BE / BBM Backend: **REST 8443 mTLS + JWT** (JWT валидация от Identity Provider)

### 3.2 Вътрешни API-и (Complaint zone)
- BBO_BE → CMS: **REST 8443 mTLS**
- BBO_BE → AI_CHATBOT: **WebSocket 8444** (за real-time чат)
- AI_CHATBOT → NLP_ENGINE: **gRPC 50051**
- AI_CHATBOT → CMS: **REST 8443**
- CMS → AI_COPILOT: **REST 8443 mTLS**
- CMS → NOTIF_SERVICE: **Kafka event (9093)** — async за decoupling
- CMS → AUDIT_LOG: **REST 8443** — sync за критични events
- Всички нови услуги → Kafka: **producer/consumer 9093 TLS+SASL**

### 3.3 AI Co-pilot context assembly
Когато специалистът работи по жалба, AI_COPILOT сглобява контекст от множество системи:
- AI_COPILOT → CORE_BANKING (клиентски профил): **SOAP/REST 8443**
- AI_COPILOT → CORE_ACC (сметки/транзакции): **SOAP 8443** през CORE_BANKING
- AI_COPILOT → CARD_SYSTEM (детайли за карта, merchant): **REST 443**
- AI_COPILOT → CRM (история на взаимодействия): **REST/OData 443**
- AI_COPILOT → CMS (подобни минали случаи): **REST 8443**

### 3.4 Нотификации (NOTIF_SERVICE)
Пълен fan-out на потвържденията:
- NOTIF → BBO_BE: **in-app push 8443** — съобщение в историята на жалбата
- NOTIF → SMTP Relay: **SMTP 587 STARTTLS** — email до клиента
- NOTIF → FCM: **HTTPS 443** — Android push
- NOTIF → APNS: **HTTPS/2 443** — iOS push

### 3.5 База данни достъп
- CMS → PostgreSQL (CMS): **JDBC 5432 TLS**
- AUDIT_LOG Service → PostgreSQL (AUDIT): **JDBC 5432 mTLS**
- CMS → MinIO (прикачени): **S3 HTTPS 9000**
- CORE_BANKING → Oracle: **JDBC 1521 TLS**
- CARD_SYSTEM / CRM → SQL Server: **TDS 1433 TLS**
- Session Service → Redis: **6379 TLS**
- Analytics → Elasticsearch: **HTTPS 9200**

### 3.6 Legacy интеграция
- CORE_ACC → Integration Bus (IBM MQ): **JMS 1414 TLS**
- ESB → external partners (при нужда): през egress firewall

---

## 4. Сигурност и съответствие

| Изискване | Реализация в архитектурата |
|---|---|
| **EBA/ESMA JC 2018 35** — одит на всяка жалба | AUDIT_LOG Service + PostgreSQL WORM с hash-chain, 7г retention |
| **DORA** — ICT resilience | Kubernetes HA, DB репликация (Oracle Data Guard, PG streaming replication), Sentinel за Redis, 3-node Kafka/ES |
| **GDPR** — защита на лични данни | Автентикация в-приложението (без КЕП), AES-256 at rest (MinIO), TLS in transit навсякъде |
| **PSD2 SCA** | OAuth2 + JWT в API Gateway, MFA през Identity Provider |
| **Мрежова сегментация** | 3 firewall-а (perimeter, internal, egress), разделени VLAN/subnet per zone |
| **Secrets management** | HashiCorp Vault, без hardcoded credentials |
| **Zero-trust вътре** | Istio service mesh с mTLS между всички pods |
| **Одит на администратори** | Bastion host като single point за SSH, SIEM алертинг |

---

## 5. Речник / Glossary

### 5.1 Инфраструктурни актьори (consistent с Задача 2, по BA упражнението)

| Съкращение | Пълно име | Описание |
|---|---|---|
| BBM_USER | Bulbank Mobile User | Клиент на банката, използващ мобилното приложение; вече автентикиран с биометрия / ПИН |
| BBM | Bulbank Mobile | Мобилното приложение на УниКредит Булбанк (iOS / Android) |
| BBO_BE | Bulbank Online Backend | Backend-ът на дигиталните канали (обслужва мобилното и уеб банкирането) |
| CORE_BANKING | — | Основна банкова система — клиенти, продукти, статуси, KYC. Legacy Java EE на JBoss EAP |
| CORE_ACC | Core Accounts Module | Модул Сметки в CORE_BANKING — баланси, транзакции, преводи |

### 5.2 Нови компоненти за процеса по жалби

| Съкращение | Пълно име | Описание |
|---|---|---|
| AI_CHATBOT | — | Чатбот модул с NLP способности за приемане и първоначална категоризация на жалби. Python/FastAPI |
| NLP_ENGINE | Natural Language Processing Engine | Модул за анализ на естествен език — категоризация, спешност, настроение, определяне на Tier. PyTorch/ONNX, GPU |
| CMS | Complaint Management System | Ядрото на процеса — регистрация, workflow (Camunda Zeebe), маршрутизиране, проследяване |
| AI_COPILOT | — | AI асистент за служителите — сглобява контекст от всички системи, предлага решения |
| NOTIF_SERVICE | Notification Service | Многоканални известия (in-app + email + push). Node.js/Express |
| AUDIT_LOG | — | Append-only одит регистър за всяко решение, одобрение и монетарно действие. Go 1.22, WORM |
| SPEC_* | Specialist | Обработващ специалист от съответния домейн: SPEC_CARDS, SPEC_ACC, SPEC_CREDIT, SPEC_DIGI |
| Specialist Workbench | — | Уеб приложение за служителите, интегрирано с CMS и AI_COPILOT. React 18 |
| Analytics / Trend Engine | — | Агрегира данни от жалби за трендове и алерти. Python, Airflow |

### 5.3 Домейн системи (не са инфраструктура)

| Съкращение | Пълно име | Описание |
|---|---|---|
| CARD_SYSTEM | Card Management System | Домейн система за дебитни/кредитни карти, картови транзакции, спорове |
| CRM | Customer Relationship Management | Microsoft Dynamics 365 on-prem — история на взаимодействия, предишни жалби |

### 5.4 Операционни системи

| Термин | Описание |
|---|---|
| RHEL 9 | Red Hat Enterprise Linux 9 — корпоративна Linux дистрибуция, поддържа Red Hat SLA, основна OS в UniCredit Group |
| Ubuntu 22.04 LTS | Long-Term Support издание на Ubuntu — използвано за Node.js / PostgreSQL / monitoring |
| Windows Server 2022 | Microsoft сървърна OS — за legacy .NET и SQL Server компоненти |
| Alpine Linux | Минималистична Linux дистрибуция — за малки Go / статични контейнери |
| RHEL UBI | Red Hat Universal Base Image — лицензно-свободна Linux база за контейнери, съвместима с RHEL |

### 5.5 Приложни сървъри и среди за изпълнение

| Термин | Описание |
|---|---|
| Tomcat 10 | Apache Tomcat — Java сървлет контейнер, поддържа Jakarta Servlet 6 (Jakarta EE 10) |
| JBoss EAP 7.4 | Red Hat JBoss Enterprise Application Platform — пълен Java EE 8 сървър |
| IIS 10 | Microsoft Internet Information Services — уеб сървър за Windows |
| NGINX 1.25 | Високопроизводителен уеб сървър и reverse proxy |
| Node.js 20 | JavaScript runtime, използван за NOTIF_SERVICE |

### 5.6 Езици, рамки и библиотеки

| Термин | Описание |
|---|---|
| Java 21 | LTS версия на Java (Virtual Threads, pattern matching) |
| Java EE 8 | Стандарт за enterprise Java (legacy); в JBoss EAP |
| Jakarta EE | Приемник на Java EE, поддържан от Eclipse Foundation |
| Spring Boot 3 | Основна Java рамка за микросервизи — auto-configuration, production-ready |
| Python 3.12 | Основен език за AI/ML компоненти |
| FastAPI | Python web framework с async поддръжка, използван за chatbot и co-pilot |
| Express | Минималистична Node.js web framework |
| Go 1.22 | Компилиран език — използван за AUDIT_LOG (висока throughput, малък footprint) |
| .NET 8 | Microsoft .NET платформа — за CARD_SYSTEM |
| PyTorch | ML framework — за training/inference на NLP модели |
| ONNX | Open Neural Network Exchange — формат за преносими ML модели |
| Airflow 2.x | Workflow orchestrator за data pipelines |
| React 18 | JavaScript UI библиотека — за Specialist Workbench |
| Camunda Zeebe | Cloud-native workflow engine — оркестрация на бизнес процеси |

### 5.7 Контейнери и оркестрация

| Термин | Описание |
|---|---|
| Kubernetes 1.29 | Open-source оркестратор на контейнери (K8s) |
| OpenShift 4.14 | Red Hat корпоративна дистрибуция на Kubernetes |
| Istio | Service mesh — mTLS, traffic management, observability между pods |
| Pod | Най-малката deployable единица в Kubernetes (1+ контейнера) |
| Sidecar | Допълнителен контейнер в pod (напр. Istio proxy за mTLS) |

### 5.8 Бази данни и съхранение

| Термин | Описание |
|---|---|
| Oracle 19c Enterprise | RDBMS за CORE_BANKING — ACID, мащабиране, Data Guard |
| PostgreSQL 15 | Open-source RDBMS — използван за CMS и AUDIT_LOG DB |
| SQL Server 2022 | Microsoft RDBMS — за CRM и CARD_SYSTEM |
| Redis 7.2 | In-memory data store — за сесии и кеш |
| MinIO | Self-hosted S3-съвместим обект-storage — за прикачени файлове |
| Elasticsearch 8 | Distributed search engine — за търсене и analytics |
| Data Guard | Oracle решение за DR репликация (primary + standby) |
| Streaming replication | Мастер-слейв репликация в PostgreSQL |
| Sentinel HA | Redis HA решение с автоматичен failover |
| WORM | Write Once Read Many — неизменяемо съхранение; в случая — append-only PostgreSQL схема |
| Hash chain | Криптографски свързан хеш във всеки запис (като blockchain) — осигурява tamper-evidence |

### 5.9 Съобщения и събития

| Термин | Описание |
|---|---|
| Apache Kafka 3.7 | Distributed event streaming platform — backbone за async комуникация |
| IBM MQ 9.3 | Enterprise message queue — за legacy интеграция с CORE_BANKING |
| ESB | Enterprise Service Bus — интеграционен слой |
| Event-driven architecture | Архитектурен стил — услугите реагират на събития, не директни извиквания |
| Producer / Consumer | Роли в message-based системи — кой изпраща и кой чете съобщенията |

### 5.10 Мрежова инфраструктура

| Термин | Описание |
|---|---|
| DMZ | Demilitarized Zone — изолирана подмрежа между публичния Интернет и вътрешната мрежа |
| WAF | Web Application Firewall — филтрира HTTP атаки (SQLi, XSS, OWASP Top 10) |
| Load Balancer | Разпределя трафика към множество backend сървъри (layer-4 или layer-7) |
| Reverse Proxy | Сървър пред backend, който абстрахира вътрешната структура, кешира, терминира TLS |
| API Gateway | Централен вход за всички API извиквания — автентикация, rate limiting, routing |
| Identity Provider | Услуга, която удостоверява самоличността на потребителите (SSO) |
| Firewall (Perimeter) | Защитна стена на периметъра на мрежата (L3/L4) |
| Firewall (Internal) | Защитна стена между вътрешните зони (L7 с deep packet inspection) |
| Firewall (Egress) | Защитна стена, контролираща изходящия трафик |
| L3/L4 | Network / Transport layer в OSI модела (IP, TCP/UDP) |
| L7 DPI | Layer 7 Deep Packet Inspection — анализ на application layer съдържанието |
| Bastion Host | Единствен sanctioned вход за SSH достъп към вътрешните системи |
| VLAN | Virtual LAN — логическо разделяне на мрежа |
| Subnet | Подмрежа с отделен IP диапазон |
| VPC Peering | Private Virtual Cloud peering — директна мрежова връзка между cloud акаунти |

### 5.11 Мрежова сигурност и автентикация

| Термин | Описание |
|---|---|
| TLS 1.3 | Transport Layer Security v1.3 — последният стандарт за криптиране на трафик |
| mTLS | Mutual TLS — и клиентът, и сървърът се удостоверяват с сертификати |
| JWT | JSON Web Token — stateless токен за автентикация (подписан, често в header) |
| OAuth2 | Стандарт за авторизация (access tokens) |
| OIDC | OpenID Connect — слой за автентикация върху OAuth2 (id_token) |
| SAML | Security Assertion Markup Language — XML-базиран SSO стандарт |
| SSO | Single Sign-On — един login за множество приложения |
| MFA | Multi-Factor Authentication — 2+ фактора за идентификация |
| RBAC | Role-Based Access Control — достъп по роли |
| PSD2 SCA | Strong Customer Authentication по PSD2 — 2 от 3 фактора за плащания |
| AES-256 | Symmetric encryption с 256-bit ключ — за данни в покой |
| HashiCorp Vault | Централизиран secrets manager (API keys, DB credentials, TLS сертификати) |
| KEP (КЕП) | Квалифициран електронен подпис — правно равностоен на ръчно подписан документ |

### 5.12 Комуникационни протоколи

| Протокол | Описание |
|---|---|
| HTTPS | HTTP over TLS — криптирана уеб комуникация |
| HTTP/2 | Втора версия на HTTP — multiplexing, header compression, server push (за APNS) |
| WebSocket | Двупосочен, постоянен канал върху HTTP/TCP — за real-time чат |
| SOAP | XML-базиран RPC протокол — използван в legacy системи |
| REST | Representational State Transfer — стандарт за HTTP API-та |
| gRPC | Google RPC — HTTP/2 + Protocol Buffers, бърз binary RPC |
| OData | Open Data Protocol — REST-базиран протокол за заявки (Microsoft стандарт) |
| JDBC | Java Database Connectivity — стандартен Java API за RDBMS достъп |
| TDS | Tabular Data Stream — Microsoft SQL Server протокол |
| JMS | Java Message Service — стандартен Java API за message queues |
| SMTP | Simple Mail Transfer Protocol — изпращане на email |
| STARTTLS | Разширение за ъпгрейд на plain-text SMTP връзка към TLS |
| S3 API | AWS Simple Storage Service API — HTTP-базиран обект storage протокол |
| SASL/SCRAM | Salted Challenge Response Authentication Mechanism — за Kafka |
| OIDC Discovery | Механизъм за откриване на OIDC endpoints (/.well-known/openid-configuration) |

### 5.13 Порт справочник (използвани в архитектурата)

| Порт | Протокол / Услуга |
|---|---|
| 22 | SSH — Bastion Host |
| 443 | HTTPS — стандартен уеб трафик |
| 587 | SMTP Submission (STARTTLS) |
| 1414 | IBM MQ (TLS) |
| 1433 | SQL Server TDS (TLS) |
| 1521 | Oracle JDBC (TLS) |
| 3000 | Grafana UI |
| 5044 | Logstash Beats input |
| 5432 | PostgreSQL (TLS) |
| 5601 | Kibana UI |
| 5671 | AMQ (TLS) |
| 6379 | Redis (TLS) |
| 8000 | Splunk |
| 8080 | Алтернативен HTTP |
| 8200 | HashiCorp Vault |
| 8443 | Алтернативен HTTPS — внутрешни mTLS API-та |
| 8444 | WebSocket (чатбот) |
| 9000 | MinIO S3 API |
| 9090 | Prometheus |
| 9093 | Kafka (TLS + SASL/SCRAM) |
| 9200 | Elasticsearch HTTPS |
| 50051 | gRPC (конвенция) |
| 55000 | Wazuh API |

### 5.14 Външни услуги и интеграции

| Термин | Описание |
|---|---|
| SendGrid / Postfix | Email delivery (SaaS или self-hosted SMTP relay) |
| FCM | Firebase Cloud Messaging — Google push нотификации за Android |
| APNS | Apple Push Notification Service — push нотификации за iOS |
| LLM | Large Language Model — напр. Claude, GPT-4, Gemini |
| Anthropic Claude | LLM от Anthropic |
| Azure OpenAI | Microsoft enterprise-grade hosting на OpenAI модели |
| UniCredit AI Platform | Вътрешна LLM платформа на UniCredit Group |
| B-Trust | Български доставчик на КЕП |
| InfoNotary | Български доставчик на КЕП |

### 5.15 Monitoring, management и DevOps

| Термин | Описание |
|---|---|
| ELK Stack | Elasticsearch + Logstash + Kibana — централизирано логване и визуализация |
| Elasticsearch | Разпределен search и analytics engine |
| Logstash | Log ingestion и трансформация |
| Kibana | Визуализация и дашбордове върху Elasticsearch |
| Prometheus | Open-source metrics и alerting система |
| Grafana | Визуализация на метрики (от Prometheus, ELK и др.) |
| GitLab | Платформа за source control + CI/CD |
| Argo CD | GitOps continuous delivery за Kubernetes |
| CI/CD | Continuous Integration / Continuous Delivery |
| SIEM | Security Information and Event Management — корелация на security events |
| Splunk | Корпоративна SIEM / логова платформа |
| Wazuh | Open-source SIEM |
| HA | High Availability — резервиране за минимално време на престой |
| DR | Disaster Recovery — възстановяване след катастрофа |

### 5.16 Регулаторни и compliance термини

| Термин | Пълно име / Закон | Описание |
|---|---|---|
| EBA | European Banking Authority | Европейски банков регулатор |
| ESMA | European Securities and Markets Authority | Европейски регулатор за ценни книжа и пазари |
| JC 2018 35 | Joint Committee Guidelines on Complaints Handling | EBA/ESMA Насоки за обработка на жалби |
| GDPR | General Data Protection Regulation | ЕС регламент за защита на лични данни |
| DORA | Digital Operational Resilience Act | ЕС акт за дигитална оперативна устойчивост |
| PSD2 | Payment Services Directive 2 | ЕС директива за платежни услуги |
| KYC | Know Your Customer | Процес за идентификация на клиентите |
| БНБ | Българска народна банка | Основен банков регулатор в България |
| КЗП | Комисия за защита на потребителите | Орган за потребителска защита |
| ПКПС | Помирителна комисия за платежни спорове | Извънсъдебна комисия за платежни спорове |
| FIN-NET | Financial Dispute Resolution Network | Мрежа за презгранично финансово разрешаване на спорове в ЕС |
| ЗЗЛД | Закон за защита на личните данни | Български имплементация на GDPR |
| ЗКИ | Закон за кредитните институции | Регулиране на банкова дейност |
| ЗПУПС | Закон за платежните услуги и платежните системи | Българска имплементация на PSD2 |
| ЗПК | Закон за потребителския кредит | Регулация на потребителското кредитиране |
| ЗКНИП | Закон за кредитите за недвижими имоти на потребители | Регулация на ипотечни кредити |

### 5.17 Общи съкращения

| Съкращение | Пълно име |
|---|---|
| SLA | Service Level Agreement — договорено ниво на обслужване |
| API | Application Programming Interface |
| RPC | Remote Procedure Call |
| UI / UX | User Interface / User Experience |
| BPMN | Business Process Model and Notation |
| UML | Unified Modeling Language |
| NLP | Natural Language Processing |
| AI | Artificial Intelligence |
| ML | Machine Learning |
| LTS | Long-Term Support |
| DPI | Deep Packet Inspection |
| DNS | Domain Name System |
| CIDR | Classless Inter-Domain Routing |
| WAF | Web Application Firewall |
| CDN | Content Delivery Network |
| DR | Disaster Recovery |
| HA | High Availability |
