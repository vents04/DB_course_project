# AI Usage Log — Course Project: Digitalization in Banking

This log tracks all steps where AI (Claude Code) was used throughout the course project, including the reasoning behind each decision.

---

## 2026-04-08 — Lecture Material Conversion & Organization

### 1. Project Structure Setup

**What was done:** Created a `lectures/` folder with 6 subfolders, one per lecture, named descriptively based on their content:

| Folder | Source PDF |
|--------|-----------|
| `01_digitalization_in_banking` | Лекция1_Дигитализация в банкирането_2026.pdf |
| `02_it_operations_cloud_containers` | Лекция 2_TU_2026.pdf |
| `03_introduction_to_business_analysis` | Introduction to Business Analysis_Feb_2026_v2.pdf |
| `04_microservices_devops_vibecoding` | Презентация Програмиране на микросервизни приложения... .pdf |
| `05_digital_banking_echannels` | TU-SOFIA_DB_eChannels.pdf |
| `06_project_management_it_processes` | ProjectManagementITprocesses.pdf |

**Why:** The original PDFs had inconsistent naming (mix of Bulgarian/English, varying formats). A standardized, numbered folder structure makes it easier to navigate and reference in future work. Each folder is self-contained with the converted markdown and extracted images. The original PDFs were removed after manually verifying the markdown extractions were correct.

### 2. PDF-to-Markdown Conversion

**What was done:** Used the `pymupdf4llm` Python library to convert all 6 lecture PDFs into markdown files with extracted images.

**Tool choice — why pymupdf4llm:**
- Specifically designed for producing LLM-friendly markdown from PDFs
- Handles image extraction natively (`write_images=True`) — saves images as PNGs and inserts relative markdown references
- Preserves text structure (headings, tables, lists) better than generic PDF-to-text tools
- Includes OCR'd text from images between `Start of picture text` / `End of picture text` markers, providing textual descriptions of diagrams/figures that LLMs can interpret without viewing the image file

**Configuration used:**
- `write_images=True` — extract and save all images
- `image_format="png"` — lossless format for diagram clarity
- `dpi=200` — higher than default (150) for readable diagrams
- Images saved to an `images/` subfolder within each lecture folder
- Image paths in markdown corrected to be relative (e.g., `images/filename.png`) so they resolve correctly when the .md file is opened from its own directory

### 3. Image Filtering & Markdown Cleanup

**What was done:** After the automated conversion, the user manually reviewed each lecture's `images/` folder and removed unnecessary images (design placeholders, decorative elements, slide backgrounds, etc.). After each lecture's images were filtered, AI updated the corresponding .md file to remove references to deleted images and clean up resulting whitespace.

**Why:** pymupdf4llm extracts every embedded image from the PDF, including non-informational ones (background patterns, logos, slide design elements). These add clutter and noise for LLM analysis. Manual filtering ensured only meaningful images (diagrams, architecture charts, process flows) were retained. The markdown cleanup was automated via regex to keep the files consistent.

**Results per lecture:**

| Lecture | Total Extracted | Kept | Removed |
|---------|----------------|------|---------|
| 01 — Digitalization in Banking | 49 | 9 | 40 |
| 02 — IT Operations, Cloud & Containers | 155 | 0 | 155 |
| 03 — Introduction to Business Analysis | 36 | 10 | 26 |
| 04 — Microservices, DevOps & VibeCoding | 119 | 7 | 112 |
| 05 — Digital Banking eChannels | 104 | 3 | 101 |
| 06 — Project Management & IT Processes | 149 | 13 | 136 |

## 2026-04-09 — Reference Materials Documentation

### 4. Documenting `other-relevant-materials/`

**What was done:** Created a `README.md` in the `other-relevant-materials/` folder describing each file's type, contents, and purpose within the course project. AI read each file (2 `.docx` files via python-docx, 1 `.xls` via xlrd, 1 `.pdf` via pymupdf) to extract content summaries.

**Why:** The folder contains instructor-provided templates and examples (product backlog template, project plan, BA exercise, credit workflow) with non-descriptive or Bulgarian-language filenames. A README provides a quick English-language reference so any team member or LLM can understand what each file is for without opening it.

### 5. Project Topics Document Conversion

**What was done:** Created an `.md` file based on the original `.docx` document containing the project variant assignments for the course. Stripped to only the general information and Variant 3 (digitalization of a complaints process), which is the variant assigned to our team.

### 6. Task 1 — Research on Digital Complaint Handling in Banking

**What was done:** Conducted web research across multiple dimensions and compiled findings into `deliverables/01_research/research.md`.

**Why this approach:** The task requires research on best practices. Rather than only describing what others do, the research was structured as: international benchmarks → comparison matrix → regulatory constraints → technology patterns → innovative proposal for UniCredit Bulbank. This mirrors real consulting deliverables and positions the project strongly by showing both awareness of the market and original thinking.

**Tools used:** WebSearch for broad discovery across banking complaint processes, regulatory frameworks, and architecture patterns; WebFetch for deep-diving into specific pages (Monzo's philosophy blog post, DBS chatbot details, Bulgarian banking regulation guide, UBB feedback form).

### 7. Firsthand Testing of Bulgarian Banks' Complaint Processes

**What was done:** The team manually tested the complaint submission process of all three top-tier Bulgarian banks — UniCredit Bulbank, UBB, and DSK Bank — through their websites and mobile apps/chatbots on 2026-04-09. Screenshots were captured at each step. Findings were integrated into the research document.

**Key findings:**
- **UniCredit Bulbank:** Web form exists, but no on-screen confirmation, no reference number, and no acknowledgment email were observed after submission. Mobile app could not be tested (requires client activation, no team member is a UCB client).
- **UBB:** Web form with structured complaint categories and on-screen confirmation with 45-day timeline. No reference number. Mobile app chatbot redirects complaint queries to the web form — no way to complain in-app.
- **DSK Bank:** Best local experience — two-email flow with immediate acknowledgment, priority triage explanation, and a reference number (#1317654). However, D.bot chatbot is buggy and directs complaint requests to the website.
- **Common gap across all three:** No Bulgarian bank handles complaints through in-app or chatbot channels. All redirect to separate web forms.

**Why:** The original research relied on web search snippets and official page content, but some claims (e.g., that UCB was "paper-form only") turned out to be inaccurate or unverifiable. Firsthand testing provided ground-truth data that strengthened the research and exposed the real competitive landscape. UBB and DSK were specifically chosen because they are the only two direct competitors to UCB in Bulgaria.

### 8. Research Iterations and Quality Improvements

**What was done:** Multiple rounds of refinement to the research document:

1. **Factual accuracy pass:** Corrected the initial claim that UCB was "paper-form only" — they do have a web form. All claims were reviewed and those based on unverified search snippets were either verified, flagged, or removed.

2. **Source attribution:** Added inline confidence tags ([Verified], [Official source], [Third-party], [General industry]) to every claim so the reader knows the provenance of each piece of information. Later simplified by removing inline annotations and keeping sources only at the end for readability.

3. **Competitor simplification:** Dropped N26 (unverified, added nothing beyond Revolut) and HSBC (well-sourced but didn't contribute unique insights to the proposal — DSK Bank already served as the "traditional bank" comparison locally). Kept Revolut (AI triage), Monzo (philosophy + specialist routing), and DBS (AI co-pilot for staff) as the three international references that directly shaped the proposal.

4. **Local benchmarking added:** UBB and DSK Bank sections added with full CX analysis, three-way Bulgarian comparison table, and chatbot/mobile app testing results.

**Why:** The research went through these iterations because the user correctly challenged unverified claims and pushed for factual rigor. Each iteration made the document more honest and more useful — moving from search-snippet assumptions to firsthand-tested data.

### 9. Task 1 — Bulgarian PDF Build

**What was done:** Translated the full research document to Bulgarian (`research_bg.md`) and generated a PDF (`research_bg.pdf`) using md-to-pdf with Mermaid diagram rendering and embedded images.

**Why:** The final deliverable needs to be in Bulgarian for the course presentation. md-to-pdf was chosen because it natively renders Mermaid diagrams and supports custom CSS styling for professional output.

### 10. Task 2 — BPM Process Diagram for Digital Complaint Handling

**What was done:** Created `deliverables/02_bpm_process/bpm_process.md` (in Bulgarian) with PDF output. The deliverable includes:
- Actor/role definitions table (7 participants: Client, AI Chatbot, Complaint System, Specialist, AI Co-pilot, Manager, Regulators)
- Full BPMN-style process diagram (Mermaid flowchart) covering all 6 phases from complaint initiation to feedback
- Detailed step-by-step descriptions for each phase with forward/backward movement rules
- Two sequence diagrams following the style from the BA exercise: (1) complaint submission flow showing Client ↔ App ↔ Chatbot ↔ NLP ↔ CMS interactions, (2) investigation and resolution flow showing CMS ↔ AI Co-pilot ↔ Specialist ↔ Core Banking interactions
- Summary tables for forward rules, backward rules, and SLA timelines
- Glossary of all terms and acronyms

**Why this approach:** The task requires a process from the client's perspective with defined steps, forward/backward rules, and actor roles. The BPM flowchart provides the high-level view, while the sequence diagrams provide the detailed system interaction view — matching the style from the BA exercise reference material. The process directly builds on the proposal from Task 1's research, maintaining consistency across deliverables.

### 11. Task 2 — BPMN 2.0 conversion + regulatory fix

**What was done:**

1. **Identified a regulatory compliance gap** in both the research and BPM diagram: the original design had the AI chatbot autonomously executing monetary actions (e.g., fee reversal, card block) based only on client acceptance. This violated EBA/ESMA JC 2018 35 (dedicated complaints management function must review every complaint), UCB's own policy, and DORA audit-trail requirements.

2. **Introduced a tiered handling model (A/B/C/D)** in the research (Section 6.2):
   - Tier A — informational only (no bank action)
   - Tier B — safe client-initiated actions (card block, notifications)
   - Tier C — AI-suggested, specialist-approved (fee refunds, compensation)
   - Tier D — full manual investigation (fraud, credit disputes, high-value disputes)

3. **Added multi-channel notifications at every touchpoint** — every confirmation is now delivered via in-app + email + push (matches DSK Bank's observed practice).

4. **Converted the BPM deliverable format:**
   - Created `complaint_process.bpmn` — BPMN 2.0 XML with collaboration (Client pool + Bank pool), 4 swim lanes (AI Chatbot, CMS, Specialist, Manager), 20 tasks, 6 gateways, 37 sequence flows, proper BPMNDI positioning
   - Loadable in bpmn.io, draw.io, Camunda Modeler
   - `bpm_process.md` restructured as a metadata/README file with actor definitions, phase tables, forward/backward rules, SLA timelines, regulatory references, and glossary

**Why this approach:** The user correctly identified the regulatory risk of chatbot-autonomous monetary actions. The tiered model makes the human-in-the-loop explicit for anything involving money or personal data, while preserving the UX benefit of AI handling informational queries and routing safe client-initiated actions. Converting to BPMN 2.0 XML makes the deliverable loadable in real BPM software (not just a rendered image), which is the industry standard for business process modeling.

### 12. Task 2 — Added sequence diagrams for system integration view

**What was done:** Added 4 PlantUML sequence diagrams alongside the existing BPMN file (existing BPMN was not modified):
- `seq_01_submission_and_registration.puml` — client login through to formal complaint registration with multi-channel notification
- `seq_02_investigation_with_copilot.puml` — AI Co-pilot context assembly across infrastructure and domain systems
- `seq_03_decision_and_execution.puml` — specialist decision, explicit approval for monetary actions, AUDIT_LOG recording, execution through CORE_BANKING/CORE_ACC, client response handling
- `seq_04_fast_path_tier_ab.puml` — Tier A/B deflection flow (no formal complaint, chatbot-handled)

**Actor model (clarified per user feedback):**
- **Infrastructure actors** (preserved from UniCredit BA exercise): BBM_USER, BBM, BBO_BE, CORE_BANKING, CORE_ACC
- **New complaint-specific services**: AI_CHATBOT, NLP_ENGINE, CMS, AI_COPILOT, NOTIF_SERVICE, AUDIT_LOG, SPEC_{CARDS/ACC/CREDIT/DIGI}
- **Domain systems** (not infrastructure, used only for specific scenarios): CARD_SYSTEM, CRM

**Why BPMN + Sequence diagrams instead of one single diagram:** BPMN answers the business-process question (who does what, in what order, under what rules); sequence diagrams answer the system-integration question (which system calls which, over time). Keeping them separate preserves readability and matches industry practice. The BA exercise from UniCredit itself uses sequence diagrams with the exact infrastructure actor set adopted here.

**Why PlantUML:** Text-based, free online viewer at plantuml.com/plantuml, version-controllable, matches the syntax style of the BA exercise reference material, renders to PNG/SVG for presentations.

### 13. Task 3 — Technology Architecture

**What was done:** Created `deliverables/03_architecture/` with two files:
- `technology_architecture.drawio` — draw.io 2.0 XML, importable into app.diagrams.net. 69 shapes + 37 labeled connections.
- `architecture.md` — metadata file with zone-by-zone breakdown, component tables (OS, tech, ports), connection details, security/compliance mapping, and glossary.

**Architecture coverage (per task.md Task 3 requirements a-d):**
- (a) Servers with OS and application servers: every component labeled with OS (RHEL 9, Ubuntu 22.04 LTS, Windows Server 2022, Alpine) and app server (Tomcat 10, JBoss EAP 7.4, IIS 10, NGINX, Kubernetes/OpenShift)
- (b) Network segmentation: 7 zones separated by 3 firewalls (perimeter, internal, egress) + WAF + Reverse Proxy + API Gateway
- (c) Technologies, protocols, and ports: every component has tech stack + port; every connection has protocol + port label
- (d) Inter-application connections: 37 labeled edges showing communication paths

**Architecture design choices:**
- Kept existing systems (BBO_BE, CORE_BANKING, CORE_ACC, CARD_SYSTEM, CRM) unchanged per the project postulate ("bank already has online channels")
- New complaint-specific services (AI_CHATBOT, NLP_ENGINE, CMS, AI_COPILOT, NOTIF_SERVICE, AUDIT_LOG, Specialist Workbench, Analytics) designed as Kubernetes-deployed microservices with Istio mTLS
- AUDIT_LOG on WORM PostgreSQL with hash chain for tamper-evidence (DORA + EBA compliance)
- Multi-channel notification fan-out via NOTIF_SERVICE (in-app + email + push) aligned with the BPM process decision (DSK Bank's model)
- Kafka event backbone for async decoupling of CMS from notifications and analytics
- External integrations (SMTP, FCM, APNS, LLM API, regulators, KEP validation) behind egress firewall whitelist

**Why single `.drawio` + single `.md`:** User explicitly requested one XML file (importable into app.diagrams.net) plus one metadata `.md` file. Keeping it in one diagram makes the architecture understandable as a whole rather than requiring the reader to mentally merge multiple views.

### 14. Task 3 — Detailed glossary

**What was done:** Expanded the glossary in `architecture.md` from 4 brief sections (~25 entries) to 17 categorized sections (~180 entries). Covers: infrastructure actors, new complaint components, domain systems, operating systems, app servers, languages/frameworks, containers/orchestration, databases, messaging, network infrastructure, security/authentication, protocols, port reference, external services, monitoring/management, regulatory/compliance, general abbreviations.

**Why:** Every term referenced in the architecture diagram (shape labels, protocol/port edge labels) or in the accompanying text is now defined in the glossary, so a reader encountering any acronym can look it up without searching externally.

### 15. Task 4 — Agile Product Backlog

**What was done:** Created `deliverables/04_project_plan/` with:
- `product_backlog.xlsx` — Excel workbook following the instructor template (`Product-backlog-template.xls`) with 5 sheets: PRODUCT BACKLOG (42 user stories, 221 story points, grouped into 6 epics, with dropdowns for priority/sprint/owner/estimate/epic), PROJECT DETAILS, DROPDOWN MENUS, ROADMAP (new sheet — sprint goals and dates), RESOURCES (team composition table + burndown chart template with actual line chart). Generated via Python + openpyxl.
- `project_plan.md` — metadata: Agile-over-Waterfall justification, Scrum team composition (13.75 FTE), epic structure (6 epics), 12-week / 6-sprint roadmap, Definition of Done, risk register, mapping back to the template structure.

**Why Agile not Waterfall:** NLP/AI components need iteration on real user data; regulatory environment (DORA, EBA) is evolving; legacy integrations are unpredictable; stakeholders need early visibility; client UX requires real-user validation. Waterfall risks (specification-heavy AI work, regulatory drift, big-bang integration) made it unsuitable.

**Stories are grouped into 6 epics** derived directly from the Task 2 BPM and Task 3 architecture, ensuring consistency across deliverables: E1 Foundation & Infrastructure, E2 Complaint Intake (Chatbot + NLP), E3 Workflow Registration & Notifications, E4 Specialist Workbench & AI Co-pilot, E5 Resolution Escalation & Audit, E6 Analytics Launch & Non-functional.

**Why extending the template is encouraged (per CLAUDE.md):** The instructor template had minimum columns; we added Epic grouping, Acceptance Criteria, and a new ROADMAP sheet for sprint goals — all useful for a real Agile project. The original column structure is preserved.

### 16. Task 4 — Methodology reversal: Agile → Waterfall

**What was done:** Replaced the Agile product backlog with a Waterfall project plan. `product_backlog.xlsx` deleted; `project_plan.xlsx` created with 6 sheets (PROJECT PLAN, PROJECT DETAILS, PHASES & SIGN-OFFS, RESOURCES, RISKS, DROPDOWN MENUS). `project_plan.md` rewritten to justify Waterfall.

**Why the change:** The user pushed back on Agile with strong arguments:
1. Regulatory compliance is **binary** — EBA/DORA/GDPR/PSD2 must be fully in place from day 1; cannot ship "compliance MVP"
2. Client/specialist expectations at launch require a complete, working system — not incremental features
3. Legacy integrations (CORE_BANKING, CARD_SYSTEM) require formal interface contracts and sequential sign-offs
4. Stakeholder sign-off gates (Legal, Compliance, Risk, Security) must happen before production

These arguments are objectively correct for a heavily-regulated banking complaint system. Agile works best for consumer products where "shippable increment" is valuable in isolation; in a regulated environment, an increment without audit trail or escalation paths is not shippable at all.

**Two-release structure** (derived from the Tier model in research Section 6.2, reinterpreted as a rollout strategy):
- **Release 1 (Level 1) — 14 months:** Compliance-Critical CMS covering Tier C/D (formal complaint handling, audit, escalation, regulatory reporting). Fully functional without AI — specialists manually categorize and research context. This is the regulatorily-sufficient baseline.
- **Release 2 (Level 2) — 8 months:** AI/UX enhancements (AI_CHATBOT, NLP_ENGINE, AI_COPILOT, Tier A/B deflection, Analytics). These optimize productivity but don't change compliance posture.

**Waterfall phases (Release 1):** P0 Initiation (1m) → P1 Requirements (2m) → P2 Design (2m) → P3 Implementation (4m) → P4 Testing (2m) → P5 Deployment (1m) → P6 Hypercare (2m). Four explicit sign-off gates (Requirements, Design, Go/no-go, Release Closure) plus GA milestone.

**Effort:** ~14.85 FTE avg across Release 1; ~9.25 FTE across Release 2. 52 WBS tasks with Gantt-style dates, predecessors, effort, and owners in the xlsx.

**Template alignment:** Product-backlog-template.xls was Agile-oriented and no longer fits. Used the `Project Plan.pdf` reference instead. The xlsx now has WBS/Gantt structure appropriate for Waterfall. Kept preserved: team composition model, risk register structure, component/epic naming.

### 17. Task 4 — Revision 3: Hybrid (Waterfall + Agile)

**What was done:** Replaced the pure Waterfall plan with a Hybrid methodology (Water-Scrum-Fall / SAFe-inspired). `project_plan.xlsx` regenerated with 7 sheets; `project_plan.md` rewritten.

**Why the change:** User asked whether Waterfall + Agile could be combined. This is a legitimate industry pattern (SAFe, Water-Scrum-Fall) used by most regulated enterprises including UniCredit Group itself. Pure Waterfall sacrificed flexibility unnecessarily; pure Agile sacrificed compliance governance. Hybrid keeps Waterfall's sign-off gates (Requirements, Design, Go/no-go, Release Closure) while running Phase 3 Implementation and Phase 4 Testing as 2-week Scrum sprints.

**Structure:**
- **Waterfall backbone** (7 phases with formal gates): P0 Initiation, P1 Requirements, P2 Design, P5 Deployment remain Waterfall-style
- **Agile delivery inside phases:**
  - P3 Implementation (4 months) = **8 Scrum sprints × 2 weeks** with 40 user stories, 197 story points, 8 epics
  - P4 Testing (2 months) = 4 test sprints × 2 weeks
  - P6 Hypercare (2 months) = Kanban flow
- **Release 2 (AI/UX)** is intentionally more Agile-heavy — single Requirements gate + single Design gate, rest is pure Scrum

**Template alignment:** Both templates from `other-relevant-materials/` are now used together — `Project Plan.pdf` drives the Waterfall WBS in PROJECT PLAN sheet, `Product-backlog-template.xls` drives the SPRINT BACKLOG sheet for the Agile portion. This is typical for SAFe projects in banking.

**Deliverables (final):**
- `project_plan.xlsx` — 7 sheets: PROJECT PLAN (Waterfall WBS with sprint-level breakdown in P3), SPRINT BACKLOG (40 stories × 8 sprints for P3), PROJECT DETAILS, PHASES & SIGN-OFFS (with delivery mode per phase), RESOURCES, RISKS (including hybrid-specific risks), DROPDOWN MENUS
- `project_plan.md` — justification comparing Hybrid vs Pure Waterfall vs Pure Agile, industry precedent (UniCredit SAFe adoption, JPMorgan, Deutsche Bank), full structure with sprint plan, Scrum ceremonies, Definition of Done

---

*This log will be updated as the project progresses.*
