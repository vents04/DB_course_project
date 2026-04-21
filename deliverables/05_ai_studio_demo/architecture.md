# Архитектура на демото
**Frontend:** React.js (SPA) + Tailwind CSS.
**Backend-as-a-Service:** Firebase.
- **Auth:** Firebase Authentication (Email/Password).
- **Database:** Cloud Firestore (NoSQL).
- **Hosting:** Firebase Hosting.
**AI Copilot:** Google Gemini API (извиква се от Firebase Cloud Function — клиентът не държи API ключ).
**State Management:** React Context API за Auth + role.
**Routing:** React Router v6 с `PrivateRoute` за `/specialist` и `/supervisor`.

> Забележка: това демо е умишлено опростено. Production архитектурата (вж. `03_architecture/`) заменя Firebase с вътрешен banking stack (PostgreSQL, JBoss, MinIO), а Gemini с self-hosted Python FastAPI услуга. Демото доказва UX и потока, не production stack-а.
