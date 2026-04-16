# Presentation Notes – Task 3: Technology Architecture

## 1. Цел на Task 3
- Да се представи логическата и технологична архитектура на дигиталната система за управление на жалби в UniCredit Bulbank.
- Фокус върху ключови компоненти, интеграции, технологии и сигурност.

## 2. Какво показва архитектурната диаграма
- Показва реалните архитектурни зони: Client Zone, DMZ, Digital Channels Zone, Complaint Services Zone, Core Banking Zone, Database Zone, External Services, Monitoring / Management.
- Визуализира конкретните системи и компоненти, тяхното разположение по зони и начина на комуникация между тях.
- Изобразява реалните комуникационни потоци и технологии (например Kafka, Istio, API Gateway, Camunda, PostgreSQL, MinIO).

## 3. Основни архитектурни зони (zones)
- Client Zone (Bulbank Mobile, Bulbank Online, външни клиенти)
- DMZ (WAF, Load Balancer, NGINX Reverse Proxy, API Gateway/Kong)
- Digital Channels Zone (BBO_BE, BBM, Notification Service)
- Complaint Services Zone (CMS, AI Chatbot, Camunda, Kafka, Notification Service, Audit)
- Core Banking Zone (Core Banking System, CRM, Card System)
- Database Zone (PostgreSQL, Oracle, Redis, MinIO)
- External Services (BNB, CPC, FIN-NET, LLM API)
- Monitoring / Management (ELK Stack, Grafana, Prometheus, Audit Trail)

## 4. Основни системи/компоненти за обяснение
- Complaint Management System (CMS)
- AI Chatbot, Camunda (workflow), Kafka (event streaming), Notification Service
- API Gateway (Kong), NGINX Reverse Proxy, WAF, Load Balancer
- Core Banking System, CRM, Card System
- PostgreSQL, Oracle, Redis, MinIO (storage)
- Monitoring & Logging: ELK Stack, Grafana, Prometheus, Audit Trail (WORM)

## 5. Ключови технологии за споменаване
- Kubernetes / OpenShift (контейнеризация и оркестрация)
- Istio service mesh (mTLS, observability, traffic control)
- Kafka (port 9093, сигурна комуникация между услуги)
- Camunda (workflow engine за процеси)
- PostgreSQL, Oracle, Redis, MinIO (storage, кеширане, документи)
- API Gateway (Kong), NGINX, WAF (Web Application Firewall)
- ELK Stack, Grafana, Prometheus (monitoring, logging)
- OAuth2, SSO, Biometric/PIN (authentication)
- LLM API (AI интеграция)

## 6. Интеграции и комуникационни потоци
- Client → WAF → Load Balancer → NGINX Reverse Proxy → API Gateway (Kong)
- API Gateway → Digital Channels (BBO_BE, BBM)
- Digital Channels → Complaint Services Zone (CMS, AI Chatbot, Camunda)
- CMS → Kafka (port 9093, event streaming), Notification Service, Audit
- AI Chatbot → LLM API (AI обработка)
- Copilot → Core Banking System, CRM, Card System
- Notification Service → клиентите (push, email, SMS)
- Външни интеграции: Regulatory reporting към BNB, CPC, FIN-NET

## 7. Сигурност
- Perimeter Firewall (между Client Zone и DMZ) и Internal Firewall (между зони)
- WAF (Web Application Firewall) за защита от външни атаки
- mTLS навсякъде (чрез Istio service mesh)
- Network segmentation по зони (няма директен достъп между Client и Database Zone)
- Няма директен достъп до базите данни от външни или клиентски системи
- Audit logging (WORM – Write Once Read Many) за непроменяеми логове
- Authentication & Authorization: OAuth2, SSO, Biometric/PIN
- GDPR compliance (лични данни)

## 8. Какво да се каже на презентация/защита
- Архитектурата е разделена на реални зони (Client Zone, DMZ, Digital Channels Zone и др.), което осигурява ясно разграничение на отговорности и сигурност.
- Всяка клиентска заявка преминава през WAF, Load Balancer, NGINX Reverse Proxy и API Gateway (Kong) – това гарантира защита и контрол на трафика.
- Complaint Management System (CMS) и AI Chatbot са в Complaint Services Zone, използват Camunda за workflow и Kafka за event streaming.
- Всички комуникации между микросервиси са защитени с mTLS чрез Istio service mesh.
- Copilot има достъп до Core Banking, CRM и Card System само през защитени вътрешни канали.
- Данните се съхраняват в PostgreSQL, Oracle, Redis и MinIO, като няма директен достъп от външни зони.
- Monitoring и Audit Trail са централизирани и непроменяеми (WORM), което гарантира проследимост и реакция при инциденти.

## 9. Кратък скрипт (1–2 минути)
"Архитектурата е организирана в реални зони – Client Zone, DMZ, Digital Channels Zone, Complaint Services Zone, Core Banking Zone и Database Zone. Всяка клиентска заявка преминава през WAF, Load Balancer, NGINX Reverse Proxy и API Gateway (Kong), което осигурява многостепенна защита. В Complaint Services Zone работят CMS, AI Chatbot, Camunda и Kafka, които автоматизират процесите и осигуряват бърза обработка на жалби. Всички микросервиси комуникират през Istio service mesh с mTLS. Copilot има достъп до Core Banking, CRM и Card System само през защитени вътрешни канали. Данните се съхраняват в PostgreSQL, Oracle, Redis и MinIO, без директен достъп от външни зони. Monitoring и Audit Trail са централизирани и непроменяеми. Тази архитектура гарантира сигурност, скалируемост и лесна поддръжка."

## 10. Примерна структура на слайдове
1. Цел на Task 3
2. Архитектурна диаграма (technology_architecture.drawio)
3. Архитектурни зони (Client Zone, DMZ, Digital Channels Zone, Complaint Services Zone, Core Banking Zone, Database Zone, External Services, Monitoring / Management)
4. Основни системи и компоненти (CMS, AI Chatbot, Camunda, Kafka, API Gateway, Core Banking, MinIO и др.)
5. Ключови технологии (Kubernetes, Istio, Kafka, Camunda, PostgreSQL, MinIO, Kong, WAF, ELK Stack и др.)
6. Интеграции и комуникационни потоци (реални стъпки от диаграмата)
7. Сигурност (firewall-и, mTLS, segmentation, WORM)
8. Какво да се каже/ключови акценти
9. Кратък скрипт
10. Въпроси и отговори
