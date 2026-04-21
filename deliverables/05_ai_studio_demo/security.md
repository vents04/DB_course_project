# Мерки за защита
- **Firestore Security Rules:**
  - Клиент: чете/пише само `complaints` където `creatorUid == request.auth.uid`. Не може да променя `status`, `reference`, `slaDueAt`, `assignedTo`, `draftResponse`, `supervisorApprovedBy`.
  - Специалист: чете `complaints` където `assignedTo == request.auth.uid`. Пише `finalResponse`, `monetary`, `status` (само в разрешени преходи).
  - Ръководител: чете всички `complaints`. Пише `supervisorApprovedBy` и финално решение на escalated случаи.
  - `complaints/{id}/audit` — append-only за всички роли; никой не може да изтрива или update-ва записи.
- **Монетарно правило:** Rule проверява, че при `status == 'responded' && monetary == true` полето `supervisorApprovedBy != null`.
- **PII в демото:** ЕГН се съхранява като стринг. В production — криптирано и never logged. В демото — `egn` не се връща в заявки извън `getUser(uid)`.
- **Gemini API ключ:** стои в Cloud Function secret, не в клиентския код.
