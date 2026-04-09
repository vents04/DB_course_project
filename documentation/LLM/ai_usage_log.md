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

---

*This log will be updated as the project progresses.*
