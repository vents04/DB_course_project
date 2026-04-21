# Колекции в Firestore

### users
- `uid`: string (Primary Key)
- `name`: string
- `email`: string
- `egn`: string
- `role`: string (`'customer' | 'specialist' | 'supervisor'`)
- `category`: string (optional, за специалисти — напр. `cards`, `payments`, `credit`)

### complaints
- `id`: string (auto-generated)
- `reference`: string (`CMPL-YYYYMMDD-XXXX`, уникален)
- `creatorUid`: string
- `creatorName`: string
- `category`: string (`cards | payments | credit | other`)
- `description`: string
- `attachments`: array<string> (URL-stubs, в демото без реален upload)
- `status`: string (виж `business-logic.md` §3)
- `slaDueAt`: timestamp
- `assignedTo`: string (specialist uid, nullable)
- `draftResponse`: string (от AI Copilot, nullable)
- `finalResponse`: string (nullable)
- `monetary`: boolean
- `monetaryAmount`: number (nullable)
- `supervisorApprovedBy`: string (uid, nullable)
- `customerResolution`: string (`'accept' | 'dispute'`, nullable)
- `disputeReason`: string (nullable)
- `createdAt`: timestamp
- `updatedAt`: timestamp

### complaints/{id}/audit (subcollection)
- `actorUid`: string
- `actorRole`: string
- `action`: string (`'created'`, `'opened'`, `'draft_generated'`, `'responded'`, `'approved_monetary'`, `'disputed'`, `'escalated'`, `'closed'`)
- `timestamp`: timestamp
- `metadata`: map (optional)
