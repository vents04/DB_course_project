# Задача 5: Google AI Studio демо

Това е **живо демо** на To-Be процеса, генерирано от Google AI Studio (Gemini) с React + Firebase stack. Целта е да покаже на защитата, че UX/UX flow-ът от `02_process/` е реализуем и готов за iteration.

## Съдържание

| Файл | Роля |
|---|---|
| `product.md` | Визия, цел, потребители |
| `requirements.md` | Функционални + нефункционални изисквания |
| `architecture.md` | Frontend + Firebase stack (демо само) |
| `auth.md` | Роли по email домейн |
| `business-logic.md` | Жизнен цикъл на жалбата |
| `data-model.md` | Firestore колекции |
| `api.md` | Firestore query shape |
| `security.md` | Firestore Rules + PII |
| `edge-cases.md` | Грешки и fallback-ове |
| `testing.md` | Тестови сценарии за защита |
| **`prompt.md`** | **Paste-ready prompt за Google AI Studio** |

## Как се използва

1. Отворете [Google AI Studio](https://aistudio.google.com/).
2. Изберете **Build** mode (или стандартен chat с Gemini 2.0/2.5).
3. Копирайте **цялото** съдържание на `prompt.md` и го пейстнете.
4. Натиснете Enter. Gemini ще изгради React + Firebase проект по спецификацията.
5. Изтеглете генерирания код, конфигурирайте Firebase проект (Auth + Firestore + Functions) и пускайте `npm install && npm run dev`.
6. За iteration ползвайте follow-up съобщения: *„add X"*, *„fix Y"*, *„refactor Z"*.

## Съответствие с production архитектурата

Демото е **умишлено опростено** и не повтаря production stack-а:

| Слой | Демо (AI Studio) | Production (`03_architecture/`) |
|---|---|---|
| Frontend | React SPA | Bulbank Mobile (native iOS/Android) |
| Auth | Firebase Email/Password | Биометрия / ПИН + OIDC |
| Backend | Firebase Cloud Functions | Spring Boot на JBoss EAP 8 |
| DB | Cloud Firestore | PostgreSQL 16 |
| AI Copilot | Gemini API (managed) | Self-hosted Python FastAPI |
| File storage | URL stubs | MinIO (S3-compatible) с object-lock |
| Мрежа | Firebase публичен | 3 firewalls + DMZ + вътрешни сегменти |

Това разделяне е умишлено: демото доказва UX и потока, production stack-ът осигурява регулаторната защита.
