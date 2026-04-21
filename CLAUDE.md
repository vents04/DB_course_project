# Course Project — Дигитализация на процеса по жалби

## Project Overview
Variant 3 of the course „Дигитализация в банкирането“: digitalizing the complaint submission and handling process for UniCredit Bulbank. Full remote, no branch visit, no КЕП required (identity is proven by in-app authentication).

**Target: 7-minute team presentation** (3 presenters × ~2:20), with the markdown deliverables extensible into a single bound Word/PDF document for print submission.

## Language
**Bulgarian throughout.** Deliverables, comments, and the final document are all in Bulgarian.

## Deliverables

| Task | Folder | File(s) | Purpose |
|---|---|---|---|
| 1 | `deliverables/01_research/` | `research.md` | Сравнение на UCB/DSK/ОББ + Revolut benchmark; извежда пазарен gap + регулаторна рамка |
| 2 | `deliverables/02_process/` | `process_and_sequence.md`, `sequence_complaint.puml` | Роли, As-Is/To-Be, правила за придвижване, BPM flowchart, sequence диаграма |
| 3 | `deliverables/03_architecture/` | `architecture.drawio`, `architecture.md` | Мрежови сегменти (DMZ + App + DB), 3 защитни стени, технологичен стек |
| 4 | `deliverables/04_project_plan/` | `project_plan.md`, `product_backlog.csv` | Agile обосновка, 4 фази, 20 User Stories |
| 5 | `deliverables/05_ai_studio_demo/` | 10 spec файла + `prompt.md` + `README.md` | Paste-ready script за Google AI Studio — React + Firebase демо на To-Be потока |
| — | `presentation/` | `presentation_outline.md` | 15-слайдов outline + speaker split |
| — | `documentation/LLM/` | `ai_usage_log.md` | Лог на AI взаимодействията |

## Design constraints (be strict about these)

- **Keep each `.md` short.** If a section grows beyond ~3 pages, it's drifting away from the 7-minute presentation target.
- **One diagram per task.** One sequence + one drawio. Don't multiply artifacts.
- **Single linear flow, no tier model.** Every complaint goes through the same path: submit → register → specialist + AI Copilot → decide → deliver → accept/dispute. No Tier A/B/C/D branching.
- **AI Copilot is a specialist tool, not a decision-maker.** It assembles context and drafts responses; the specialist always accepts or corrects the draft. Monetary actions require supervisor approval. This is the EBA/GL/2015/18 line.

## When expanding into the print document

The four `.md` files + diagrams map directly to a Word document with this TOC:

1. Заглавна страница
2. Увод
3. Проучване (from `research.md`)
4. Сравнение на аналогичен процес (extracted from research + process docs)
5. Sequence диаграма (from `process_and_sequence.md` + rendered `.puml`)
6. Архитектура (from `architecture.md` + rendered `.drawio`)
7. Проектен план (from `project_plan.md`)
8. Заключение
9. Източници

When asked to "generate the printed document", assemble these in order into a single `.docx` / `.md` and render the diagrams as embedded images.

## What NOT to do

- Don't reintroduce the Tier A/B/C/D model. Linear flow only.
- Don't add a Waterfall/hybrid track. Go Agile-only.
- Don't add HSM/QES infrastructure. Complaints do not require QES.
- Don't add multiple sequence diagrams. One PlantUML file covering the 5-stage flow with monetary and dispute branches is enough.
- Don't extend the backlog beyond ~20 stories.
- Don't expand the regulatory section beyond the three citations (ЗПУПС чл. 174 ал. 1 и 4, EBA/GL/2015/18, GDPR чл. 5).

## Presentation

- **7 min total, ~2:20/person**
- **15 slides**: Title, Agenda, 4 divider slides, content slides for each task section, and conclusion (see `presentation/presentation_outline.md`)
- Speaker split: P1 = slides 1–8 (research + regulatory), P2 = slides 9–12 (process + architecture), P3 = slides 13–15 (plan + conclusion)

## AI Usage Log

**ALWAYS** update `documentation/LLM/ai_usage_log.md` after completing any significant work. Log each broad step with reasoning. This is required by course mentors.
