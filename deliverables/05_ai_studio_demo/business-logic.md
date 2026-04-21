# Процеси
1. **Регистрация на жалба:** При `addDoc` в `complaints` системата задава:
   - `reference` = `CMPL-{YYYYMMDD}-{4-digit random}`.
   - `slaDueAt` = createdAt + 3 работни дни.
   - `status` = `registered`.
   - `assignedTo` = първи `specialist` по категория (round-robin или fallback).
2. **AI Copilot draft:** При първо отваряне на жалба от специалист, frontend извиква Cloud Function, която (а) изважда контекста (клиентски данни от `users`, предишни жалби), (б) изпраща prompt към Gemini, (в) пише черновата в `complaints.draftResponse`.
3. **Жизнен цикъл на статуса:**
   - `registered` → `investigating` (при отваряне от специалист)
   - `investigating` → `pending_supervisor` (ако `monetary: true`)
   - `pending_supervisor` → `investigating` (при одобрение) или `rejected_monetary` (при отказ)
   - `investigating` → `responded` (при изпращане на отговор)
   - `responded` → `accepted` (клиент приема) или `disputed` (клиент оспорва)
   - `disputed` → `escalated` → `closed` (ръководител взема финално решение)
   - `accepted` → `closed`
4. **Монетарно действие:** Специалист не може да прати отговор с `monetary: true` без поле `supervisorApprovedBy` — правилото е в Firestore Security Rules.
5. **Audit log:** Всяка смяна на статус пише append-only запис в подколекцията `complaints/{id}/audit` с `actorUid`, `action`, `timestamp`.
