# Задача 4: Проектен план — Дигитализация на процеса по жалби

## Файлове в тази директория

| Файл | Описание |
|---|---|
| `project_plan.xlsx` | Hybrid Waterfall + Agile проектен план. 7 sheet-а: PROJECT PLAN, SPRINT BACKLOG, PROJECT DETAILS, PHASES & SIGN-OFFS, RESOURCES, RISKS, DROPDOWN MENUS |
| `project_plan.md` | Този файл — обосновка на hybrid методологията, two-release стратегия, фази, спринтове, team composition |

## Как да отворите файла

- **Microsoft Excel** (препоръчано — всички цветове и графики се виждат)
- **LibreOffice Calc** / **Google Sheets** / **Apple Numbers**

---

## 1. Избор на методология: Hybrid (Waterfall governance + Agile delivery)

Този проект използва **хибридна методология** — Waterfall за governance и стейкхолдер sign-offs, Agile (Scrum) за delivery вътре в ключовите фази. Популярно наричан **Water-Scrum-Fall** или **SAFe-inspired hybrid** — стандартен подход за регулирани enterprise проекти.

### 1.1 Защо Hybrid, а не чист Waterfall или Agile

| Критерий | Pure Waterfall | Pure Agile | **Hybrid** |
|---|---|---|---|
| Регулаторно съответствие (binary) | ✅ | ❌ | ✅ (governance gates запазени) |
| Стейкхолдер sign-off gates | ✅ | ❌ | ✅ (Compliance, Legal, Risk, Security) |
| Integration с регулирани legacy системи | ✅ | ❌ | ✅ (формални interface contracts в P2) |
| Client expectations за пълна система при launch | ✅ | ❌ | ✅ (Release 1 = пълен production-ready MVP) |
| Регулаторен одит (frozen artifacts) | ✅ | ❌ | ✅ (artifacts frozen per gate) |
| Гъвкавост при integration surprises | ❌ | ✅ | ✅ (sprint retrospectives + rebalancing) |
| Continuous stakeholder visibility | ❌ | ✅ | ✅ (sprint demos to PO/Compliance) |
| Team morale / retention | ⚠️ Marathon feel | ✅ | ✅ (incremental wins всяка 2 седмици) |
| Early bug detection | ❌ (в края на P3) | ✅ | ✅ (вътре в sprint-ите) |
| UX feedback от реални специалисти | ❌ (само на UAT) | ✅ | ✅ (continuous demos) |

### 1.2 Реален прецедент — банки ползват hybrid

- **UniCredit Group** използва SAFe (Scaled Agile Framework) в стратегическия си план 2022-2024
- **JPMorgan Chase**, **Deutsche Bank**, **Capital One** — всички адоптират Water-Scrum-Fall за регулирани системи
- Повечето проекти подлежащи на DORA supervision използват hybrid подход

### 1.3 Структура на hybrid-а

```
┌─── P0 ──┐ ┌─── P1 ──┐ ┌─── P2 ──┐
│Initiate │ │ Reqmts  │ │ Design  │         <- Waterfall (linear, gates)
│         │ │ GATE 1✋│ │ GATE 2✋│
└─────────┘ └─────────┘ └─────────┘

┌─────────── P3 Implementation ────────────┐
│ Sprint 1→2→3→4→5→6→7→8 (2 седмици всеки)│  <- 🌀 AGILE (Scrum)
│ [backlog, standups, reviews, retros]     │
└──────────────────────────────────────────┘

┌── P4 Testing ──┐ ┌── P5 ──┐ ┌── P6 ──┐
│ 4 test sprints │ │Deploy  │ │ Hyper- │    <- Agile testing + Waterfall deploy + Kanban
│ GATE 3✋      │ │GO LIVE🎉│ │  care  │
└────────────────┘ └────────┘ └────────┘
```

**Waterfall фази** (с формални gate-ове): P0, P1, P2, P5
**Agile delivery** (вътре във фазите): P3 (8 Scrum sprints), P4 (4 test cycles), P6 (Kanban)

---

## 2. Two-release rollout стратегия

Проектът е разделен на **две последователни releases**, следвайки tiered модела от research-а (Задача 1, Section 5.2):

| Release | Обхват (по Tier модел) | Стойност | Времетраене |
|---|---|---|---|
| **Release 1 — Level 1: Compliance-Critical CMS** | Tier C + Tier D (формални жалби) | Пълно регулаторно съответствие; клиентите могат да подават жалби in-app; специалисти ръчно категоризират и изследват контекста | **14 месеца** (2026-05 → 2027-06) |
| **Release 2 — Level 2: AI / UX Enhancements** | Tier A + Tier B (deflection) + AI Co-pilot | AI_CHATBOT, NLP_ENGINE, AI_COPILOT, Tier A/B самообслужване, Analytics | **8 месеца** (2027-07 → 2028-02) |

**Обща програма: 22 месеца**

**Release 1 е пълно compliant без AI** — регулаторите получават baseline, който работи от ден 1.
**Release 2 добавя оптимизации** — AI не променя compliance posture, layer върху стабилния Level 1.

**Release 2 е по-Agile-heavy** — само по един gate за Requirements и Design, останалото — pure Scrum. Регулаторният риск е нисък, защото core compliance controls вече работят.

---

## 3. Waterfall фази (Release 1)

| Фаза | Delivery mode | Времетраене | Ключови deliverables | Gate |
|---|---|---|---|---|
| **P0** Initiation | Waterfall | 1 месец | Charter, Team | Kickoff |
| **P1** Requirements Analysis | Waterfall | 2 месеца | Business + Regulatory + NFR + Personas + **initial Product Backlog** | ✋ **GATE 1** |
| **P2** Design | Waterfall | 2 месеца | Architecture, Data model, UI/UX, APIs, Security + **sprint-level estimation** | ✋ **GATE 2** |
| **P3** Implementation | 🌀 **AGILE (Scrum)** | 4 месеца = **8 спринта × 2w** | User stories delivered sprint-by-sprint; демо на PO | — (continuous) |
| **P4** Testing | 🌀 **AGILE (test cycles)** | 2 месеца = **4 test sprints × 2w** | SIT, Compliance, Security, Perf, UAT, Regulator review | ✋ **GATE 3** — Go/no-go |
| **P5** Deployment | Waterfall + Kanban | 1 месец | Prod deploy, Pilot 5%, GA | 🎉 **GO LIVE** |
| **P6** Hypercare | 🌀 Kanban | 2 месеца | Incident resolution, Tuning, Retro + Release 2 backlog prep | ✋ **GATE 4** |

---

## 4. Agile delivery inside P3 (Implementation) — 8 Sprints

Phase 3 е single most important delivery period. Управлява се като **Scrum project** със собствен Product Owner (от Complaints dept), Scrum Master (може да е PM-а или dedicated) и 8 спринта по 2 седмици. Backlog-ът е **сериализирано prepared** в P1/P2 (initial backlog + sprint-level estimation) и се изпълнява incrementally в P3.

### 4.1 Sprint план

| Sprint | Dates | Sprint Goal | Key Epics |
|---|---|---|---|
| **Sprint 1** | 2026-10-01 → 2026-10-14 | Infrastructure Foundation готов | E1 (K8s, DBs, Kafka, Vault, MinIO, CI/CD) |
| **Sprint 2** | 2026-10-15 → 2026-10-28 | CMS Core може да регистрира жалба | E2 (ref#, workflow, Camunda Zeebe) |
| **Sprint 3** | 2026-10-29 → 2026-11-11 | Audit + Compliance Core работят | E3 (AUDIT_LOG, RBAC, retention, regulatory mapping) |
| **Sprint 4** | 2026-11-12 → 2026-11-25 | Notifications multi-channel работят | E4 (NOTIF_SERVICE, email/push/in-app) |
| **Sprint 5** | 2026-11-26 → 2026-12-09 | Specialist Workbench v1 | E5 (queue, detail, decision flow, approval) |
| **Sprint 6** | 2026-12-10 → 2026-12-23 | Client-facing end-to-end | E6 (BBM + BBO + attachments + tracking) |
| **Sprint 7** | 2027-01-02 → 2027-01-15 | Core Banking + Card integration | E7 (adapters, compensation via CORE_ACC) |
| **Sprint 8** | 2027-01-16 → 2027-01-29 | Reporting + Escalation + Polish | E8 (БНБ/EBA reports, manager review, survey) |

### 4.2 Sprint backlog overview

**40 user stories** групирани в **8 епика**, общо **197 story points**, **~740 часа** implementation effort.

Епиките съответстват на компонентите от research-а (Задача 1) и архитектурата (Задача 3):

| Epic | Име | Sprint |
|---|---|---|
| **E1** | Foundation & Infrastructure | Sprint 1 |
| **E2** | Core CMS (Registration + Workflow) | Sprint 2 |
| **E3** | Audit & Compliance Core | Sprint 3 |
| **E4** | Notifications Multi-channel | Sprint 4 |
| **E5** | Specialist Workbench | Sprint 5 |
| **E6** | Client-facing (BBM + BBO) | Sprint 6 |
| **E7** | Core Banking + Card Integration | Sprint 7 |
| **E8** | Reporting, Escalation & Polish | Sprint 8 |

Пълният backlog — виж sheet **SPRINT BACKLOG** в `project_plan.xlsx`.

### 4.3 Scrum ceremonies

| Ceremony | Честота | Участници | Цел |
|---|---|---|---|
| Sprint Planning | Start на sprint | Целият екип + PO | Избор на stories от backlog за sprint |
| Daily Standup | Всеки ден, 15 мин | Dev team + SM | Progress, blockers |
| Sprint Review | Край на sprint | Екип + PO + Стейкхолдери (вкл. Compliance) | Demo на завършени stories |
| Sprint Retrospective | Край на sprint | Dev team + SM | Continuous improvement |
| Backlog Refinement | Middle of sprint | PO + BA + Tech Lead | Подготовка на следващия sprint backlog |

---

## 5. Agile delivery inside P4 (Testing) — 4 Test Cycles

Phase 4 също се изпълнява като Agile test sprints:

| Test Cycle | Dates | Focus |
|---|---|---|
| T1 | 2027-02-01 → 2027-02-12 | SIT end-to-end testing |
| T2 | 2027-02-15 → 2027-02-26 | Compliance + Security (SAST/DAST/pen test) |
| T3 | 2027-03-01 → 2027-03-12 | Performance + UAT with real specialists |
| T4 | 2027-03-15 → 2027-03-26 | Regulator review + residual fixes |

Всеки test cycle завършва с test report, reviewed от QA Lead + Compliance. Gate 3 (Go/no-go) се взима на 2027-03-31.

---

## 6. Team composition

### Release 1 (Level 1) — ~15.85 FTE средно

| Роля | FTE | Отговорност |
|---|---|---|
| Project Sponsor | 0.1 | CCO |
| **Project Manager / Scrum Master** | 1 | **Управлява Waterfall gates И фасилитира спринтовете** (hybrid dual role) |
| **Product Owner** | 1 | От Complaints dept — владее backlog-а, приема stories |
| Business Analyst | 1 | Изисквания, Tier model |
| Compliance Advisor | 0.5 | EBA, BNB, DORA, GDPR |
| Legal Advisor | 0.25 | КЕП, ЗЗЛД, договори |
| Tech Lead / Architect | 1 | Архитектура, code reviews |
| Backend Engineer | 4 | Java/Spring Boot, Camunda, integrations |
| Frontend Engineer | 1 | React — Specialist Workbench |
| Mobile Engineer | 1 | iOS + Android |
| QA Engineer | 2 | Manual + automation |
| DevOps / SRE | 1 | K8s, CI/CD, Vault |
| Security Engineer | 0.5 | Threat model, pen test |
| UX Designer | 0.5 | Figma, prototypes, UAT support |
| Support Team | 1 | Hypercare P6 only |

**Новото в hybrid:** Product Owner (от Complaints dept) присъства в Scrum ceremonies и приема stories. Scrum Master може да е същият PM или dedicated role — зависи от bandwidth-а.

### Release 2 (AI-heavy) — ~9.25 FTE

| Роля | FTE |
|---|---|
| Project Manager | 1 |
| Product Owner | 0.5 |
| BA | 0.5 |
| Tech Lead | 1 |
| **AI/ML Engineer** | **3** |
| Backend Engineer | 2 |
| QA Engineer | 1 |
| DevOps/SRE | 0.5 |
| Compliance Advisor | 0.25 |

---

## 7. Sign-off gates

| Gate | Kога | Какво се валидира | Sign-off |
|---|---|---|---|
| Kickoff | Край на P0 | Charter, scope, budget | Sponsor |
| **✋ GATE 1** | Край на P1 | Requirements + initial Product Backlog | Compliance, Legal, Risk, Business |
| **✋ GATE 2** | Край на P2 | Architecture, Design, sprint-level estimates | Architecture Board, Security |
| Sprint Reviews | Край на всеки sprint (P3) | Stories demo-ed и приети | PO + Stakeholders |
| **✋ GATE 3** | Край на P4 | Go/no-go за production | Steering Committee |
| **🎉 GO LIVE** | Край на P5 | GA решение | Project Sponsor |
| **✋ GATE 4** | Край на P6 | Release 1 приет | Steering Committee |
| (Release 2 gates по-леки — 2 gates: Req & Design) | | | |

---

## 8. Ключови рискове (hybrid-specific)

| Риск | Вероятност × Ефект | Мярка |
|---|---|---|
| **Hybrid methodology confusion** — екипът мисли, че е pure Agile и пренебрегва gates | Med × Med | Clear expectations при kickoff; явна комуникация за gates |
| **Velocity под-очаквана** в спринтовете на P3 | Med × Med | Sprint retrospectives; scope rebalancing (stories с нисък приоритет се отлагат за Release 2) |
| **Technical debt** от спринт скорост | Med × Med | 20% capacity за refactoring всеки sprint; DoD включва debt cleanup |
| **Integration с CORE_BANKING** отнема повече от Sprint 7 | High × High | Early POC в P2; Sprint 7 е dedicated за integration; buffer в Sprint 8 |
| **Регулаторна промяна** по време на проект | Med × High | Compliance Advisor мониторира; buffer в P4 |

(Пълна таблица — виж sheet **RISKS**)

---

## 9. Definition of Done (Sprint-level)

Story е DONE, когато:
1. ✅ Код ревюиран и merge-нат
2. ✅ Unit tests покритие ≥ 80%
3. ✅ Integration tests минават в CI
4. ✅ Deployed в QA среда и тестван от QA
5. ✅ Документация обновена
6. ✅ Security scan (SAST + dependency check) без P1/P2
7. ✅ Приет от PO в Sprint Review
8. ✅ Audit events записани в AUDIT_LOG (където е приложимо)
9. ✅ UI text в БГ + EN
10. ✅ Без технически дълг записан в tracker

---

## 10. Key milestones

| Milestone | Date | Description |
|---|---|---|
| Project start | 2026-05-04 | Kickoff |
| Requirements sign-off | 2026-07-31 | ✋ GATE 1 |
| Design sign-off | 2026-09-30 | ✋ GATE 2 |
| Sprint 1 start | 2026-10-01 | 🌀 Agile delivery begins |
| Sprint 8 complete | 2027-01-29 | P3 done |
| Go/no-go | 2027-03-31 | ✋ GATE 3 |
| **Release 1 GA** | **2027-04-30** | 🎉 Production launch |
| Release 1 closed | 2027-06-30 | ✋ GATE 4 |
| Release 2 start | 2027-07-01 | AI enhancement project |
| Release 2 GA | 2028-02-29 | AI components live |

---

## 11. Съответствие с шаблона

Шаблонът `other-relevant-materials/Product-backlog-template.xls` е Agile-ориентиран — **използван е directly в sheet-а SPRINT BACKLOG** (столбове: User Story ID, User Story, Estimate SP, Priority, Sprint, Task Owner, Estimated Effort). Допълнителните столбове (Epic, Acceptance Criteria) са extension на шаблона — предварително препоръчани от инструктора.

Waterfall backbone използва `Project Plan.pdf` като референция за Gantt-style WBS структурата в PROJECT PLAN sheet-а.

**Hybrid проектът съчетава двата шаблона**, което е типично за SAFe / Water-Scrum-Fall проекти.

| Sheet | Произход | Използван за |
|---|---|---|
| PROJECT PLAN | Project Plan.pdf (Gantt) | Waterfall WBS backbone |
| SPRINT BACKLOG | Product-backlog-template.xls | Agile delivery в P3 |
| PROJECT DETAILS | Двата шаблона | Project metadata |
| PHASES & SIGN-OFFS | Нов | Gate overview |
| RESOURCES | Двата шаблона | Team composition + effort |
| RISKS | Нов | Hybrid-specific риск анализ |
| DROPDOWN MENUS | Двата шаблона | Standardized values |
