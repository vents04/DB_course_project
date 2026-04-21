# Google AI Studio — Paste-Ready Prompt

> Как се използва: копирайте **всичко** под разделителя в Google AI Studio (Build mode или chat с Gemini 2.0/2.5), натиснете Enter и оставете AI Studio да изгради демото. При нужда от повторни итерации, ползвайте follow-up съобщения от типа „add [X]" или „fix [Y]".

---

# Build a demo web app — „Bulbank Complaints"

You are building a **React + Firebase single-page application** that demonstrates an in-app complaint handling workflow for a bank. The goal is to showcase the full complaint lifecycle — submission, AI-assisted investigation, specialist resolution, customer feedback — without requiring branch visits or qualified electronic signatures.

Follow the specification below literally. Do not invent features outside it. Use Bulgarian for all user-facing UI strings; keep code identifiers in English.

## Product
- **Name:** Bulbank Complaints Demo.
- **Vision:** In-app complaint lifecycle without branch visit or КЕП.
- **Users:** Customers (any email), Specialists (`@ucb.bg`), Supervisors (`@supervisor.ucb.bg`).

## Tech stack
- React 18 (Vite or CRA) + React Router v6 + React Context for auth/role state.
- Tailwind CSS for styling (responsive, mobile-first).
- Firebase: Authentication (Email/Password), Cloud Firestore, Cloud Functions (Node 20), Hosting.
- Gemini API (`gemini-2.0-flash`) called from a Cloud Function. API key stored as Cloud Function secret — never in client code.

## Roles — auto-assigned on registration by email domain
- `@supervisor.ucb.bg` → `role: supervisor`
- `@ucb.bg` (without `supervisor.` prefix) → `role: specialist`
- anything else → `role: customer`

## Routes and guards
- `/` — landing (login/register).
- `/my-complaints` — customer dashboard (list + detail).
- `/new-complaint` — customer submission form.
- `/specialist` — specialist queue and case detail. `PrivateRoute role="specialist"`.
- `/supervisor` — supervisor queue and case detail. `PrivateRoute role="supervisor"`.
- Wrong role → redirect to the role's own dashboard.

## Firestore collections

### `users`
`uid`, `name`, `email`, `egn` (10-digit string, validated), `role`, `category` (optional, for specialists: `cards | payments | credit | other`).

### `complaints`
`id`, `reference` (format `CMPL-YYYYMMDD-XXXX`, unique, 4-digit random suffix), `creatorUid`, `creatorName`, `category`, `description`, `attachments` (string[], URL stubs only — no real upload in demo), `status`, `slaDueAt` (timestamp = createdAt + 3 business days), `assignedTo` (specialist uid or null), `draftResponse` (from Gemini), `finalResponse`, `monetary` (bool), `monetaryAmount` (number, nullable), `supervisorApprovedBy` (uid, nullable), `customerResolution` (`'accept' | 'dispute'`), `disputeReason`, `createdAt`, `updatedAt`, `slaWarning` (bool).

### `complaints/{id}/audit` (subcollection, append-only)
`actorUid`, `actorRole`, `action` (one of `created`, `opened`, `draft_generated`, `responded`, `approved_monetary`, `disputed`, `escalated`, `closed`), `timestamp`, `metadata` (map).

## Status lifecycle (strict, enforced by Firestore Rules)
`registered` → `investigating` → (`pending_supervisor` → `investigating` if approved, or `rejected_monetary` if denied) → `responded` → (`accepted` → `closed`) OR (`disputed` → `escalated` → `closed`).

## Business logic
1. **On complaint create** — Cloud Function trigger:
   - Generate `reference` in format `CMPL-{YYYYMMDD}-{random 4 digits}`.
   - Set `slaDueAt` = now + 3 business days (skip Sat/Sun).
   - Set `status = 'registered'`.
   - Pick a specialist by `category` round-robin; if none available, leave `assignedTo = null`.
   - Write `audit` entry `action: 'created'`.
2. **Specialist opens case** — client calls `openComplaint(id)`:
   - Set `status = 'investigating'`, write `audit: 'opened'`.
   - If `draftResponse` is empty, call Cloud Function `generateDraft(id)`:
     - Fetch creator profile + last 3 complaints for context.
     - Call Gemini with a Bulgarian prompt: *"Ти си AI Copilot на специалист в банка. Въз основа на следния контекст, предложи кратък професионален отговор (под 150 думи) на жалбата. Контекст: {description, category, creator history}. Отговорът трябва да е емпатичен, конкретен и на български."*
     - Write result to `draftResponse`; write `audit: 'draft_generated'`.
3. **Specialist submits response** — form with `finalResponse`, optional `monetary` checkbox + `monetaryAmount` input:
   - If `monetary = false`: set `status = 'responded'`, write `audit: 'responded'`.
   - If `monetary = true` and `supervisorApprovedBy = null`: set `status = 'pending_supervisor'`, do NOT mark as responded yet.
4. **Supervisor reviews monetary** — approves or denies in `/supervisor`:
   - Approve: write `supervisorApprovedBy = uid`, `status` → `investigating`, specialist now sees "Send" enabled; `audit: 'approved_monetary'`.
   - Deny: `status = 'rejected_monetary'`, specialist sees reason and rewrites.
5. **Customer reviews response** — sees `finalResponse` in `/my-complaints`, clicks either:
   - "Приемам" → `customerResolution = 'accept'`, `status = 'closed'`, `audit: 'closed'`.
   - "Оспорвам" → requires `disputeReason` (min 20 chars) → `status = 'disputed'` → auto-transition to `escalated`; `audit: 'disputed'` + `escalated'`.
6. **Supervisor resolves escalation** — writes final decision, `status = 'closed'`, `audit: 'closed'`.

## Firestore Security Rules (must enforce)
- Customer: read/write own `complaints` (where `creatorUid == request.auth.uid`), but CANNOT modify `status`, `reference`, `slaDueAt`, `assignedTo`, `draftResponse`, `finalResponse`, `supervisorApprovedBy`. Can only write `customerResolution` + `disputeReason` in valid transitions.
- Specialist: read `complaints` where `assignedTo == request.auth.uid`. Can write `finalResponse`, `monetary`, `monetaryAmount`, and `status` only for allowed transitions.
- Supervisor: read all `complaints`. Can write `supervisorApprovedBy`, `status` on escalated cases.
- All: `complaints/{id}/audit` is append-only — `create` allowed, `update`/`delete` denied for everyone.
- Monetary guard: prevent `status` → `responded` when `monetary == true` and `supervisorApprovedBy == null`.

## UI requirements
- **Landing:** simple login/register form with EGN validation (10 digits).
- **Customer dashboard:** list of complaints showing reference, category, status badge, SLA due date (with color coding — green >2 days, amber 1–2 days, red <1 day or overdue). Detail view shows timeline of audit entries.
- **New complaint form:** category dropdown (`cards | payments | credit | other`), description (min 30 chars), attachment URL stubs.
- **Specialist queue:** table of assigned cases, sortable by `slaDueAt`. Case detail shows customer info (name, EGN masked as `XXXXXX1234`), description, AI draft (editable textarea), `monetary` checkbox + amount, "Send" button.
- **Supervisor dashboard:** two tabs — "Pending monetary approval" and "Escalated disputes". Each case shows full audit log and action buttons (Approve/Deny for monetary; Resolve for escalations).
- **Status badges:** color-coded across all views (registered = gray, investigating = blue, pending_supervisor = amber, responded = purple, accepted = green, disputed = red, escalated = red border, closed = gray with strikethrough).
- **Real-time updates:** use Firestore `onSnapshot` — no manual refresh needed.

## Edge cases (implement all)
- Gemini timeout/error → specialist sees "Generate draft" button with fallback to manual composition; case is not blocked.
- SLA warning: scheduled Cloud Function marks `slaWarning: true` when `slaDueAt - now < 1` business day → amber badge in queue.
- Invalid EGN → inline form error, no submission.
- Unauthorized route access → redirect to role's home.
- Disallowed status transition → Firestore Rules reject; UI toast "Не е разрешен преход".
- Monetary action without approval → UI toast "Необходимо одобрение от ръководител"; Send button disabled.
- Dispute without reason → form validation blocks submission.

## Testing (must work end-to-end)
1. Register three users — one per role; verify routing by domain.
2. Customer creates a complaint → reference number appears; SLA badge green.
3. Specialist opens → AI draft renders within 3s; specialist edits and sends (non-monetary) → status `responded`.
4. Customer accepts → status `closed`; audit log has 5+ entries in correct order.
5. Second complaint: specialist marks monetary + amount → status `pending_supervisor`; supervisor approves → status returns to `investigating`; specialist sends → customer sees response.
6. Third complaint: customer disputes with reason → status `disputed` → `escalated`; supervisor resolves → `closed`.
7. Firestore Rules rejection: attempt a forbidden direct write from console → rejected.

## Non-goals (do not implement)
- Real file upload (use URL stubs only).
- КЕП / digital signature integration (auth is email/password for demo).
- Integration with real core banking (CBS) — simulate customer history with sample seed data.
- Regulatory reporting exports (out of demo scope).
- Push notifications to mobile (use in-app live updates only).

---

Begin by scaffolding the project structure, then implement in this order: (1) auth + role detection, (2) Firestore schema + rules, (3) customer submission flow, (4) specialist queue + Gemini draft, (5) supervisor approval flow, (6) customer accept/dispute flow, (7) audit log rendering, (8) SLA warning scheduler.
