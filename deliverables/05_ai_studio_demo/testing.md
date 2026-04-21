# Тестови сценарии
1. **Регистрация с различни домейни:** `@ucb.bg` → специалист portal; `@supervisor.ucb.bg` → supervisor portal; `gmail.com` → клиентски изглед.
2. **Подаване на жалба:** клиентът попълва форма, получава референтен номер `CMPL-YYYYMMDD-XXXX` и вижда обявен SLA.
3. **AI Copilot:** специалистът отваря жалба; в рамките на 3 секунди се визуализира Gemini draft; специалистът го редактира и изпраща.
4. **Монетарно действие (happy path):** специалист маркира `monetary: true`, въвежда сума; жалбата отива в supervisor queue; supervisor одобрява; `supervisorApprovedBy` се попълва; specialist довършва изпращането; клиент получава отговора.
5. **Монетарно действие (блокировка):** опит да се изпрати отговор с `monetary: true` без supervisor одобрение → Firestore Rules отказ + UI съобщение.
6. **Оспорване → ескалация:** клиентът натиска „Оспорвам" + причина; status → `disputed` → `escalated`; supervisor dashboard показва жалбата; supervisor пише финално решение; status → `closed`.
7. **Audit log:** след пълен жизнен цикъл, `complaints/{id}/audit` съдържа подредени записи: `created`, `opened`, `draft_generated`, `responded` (или `approved_monetary` + `responded`), `accepted`/`disputed`, `closed`.
8. **SLA warning:** симулирано настъпване на `slaDueAt - 1 ден` → жалбата получава бейдж в двете dashboard-а.
