# Course Project — Дигитализация на процеса по жалби (UniCredit Bulbank)

Курсов проект по дисциплина „Дигитализация в банкирането“. Тема: **Вариант 3 — Дигитализация на процеса по подаване и обработка на жалби**.

## Цел

- **Презентация: 7 минути общо**, 3 презентатора, по ~2:20 всеки.
- Всеки deliverable е написан *кратко* (1–3 страници), но *разширяем* — същите файлове ще бъдат консолидирани в единен Word/PDF документ за печат.

## Структура

```
course_project_v2/
├── README.md                              ← този файл
├── CLAUDE.md                              ← указания за AI асистент
├── documentation/
│   └── LLM/
│       └── ai_usage_log.md                ← Лог на AI взаимодействията
├── deliverables/
│   ├── 01_research/
│   │   └── research.md                    ← Задача 1: проучване (3 BG банки + Revolut)
│   ├── 02_process/
│   │   ├── process_and_sequence.md        ← Задача 2: процес, роли, правила, BPM flow
│   │   └── sequence_complaint.puml        ← PlantUML sequence диаграма
│   ├── 03_architecture/
│   │   ├── architecture.drawio            ← Задача 3: diagrams.net XML (7 зони)
│   │   └── architecture.md                ← зона-по-зона обяснение
│   └── 04_project_plan/
│       ├── project_plan.md                ← Задача 4: Agile обосновка + 4 фази
│       └── product_backlog.csv            ← 20 User Stories, 6 спринта
└── presentation/
    └── presentation_outline.md            ← 15-слайдов outline + разделение на говорителите
```

## Как се чете всяка задача

1. **Задача 1 ([`research.md`](deliverables/01_research/research.md))** — сравнение на процесите по жалби при UniCredit Bulbank, DSK Bank и ОББ, с международен benchmark (Revolut). Извежда **пазарния gap** — липсата на in-app подаване.
2. **Задача 2 ([`process_and_sequence.md`](deliverables/02_process/process_and_sequence.md) + [`sequence_complaint.puml`](deliverables/02_process/sequence_complaint.puml))** — роли, As-Is vs To-Be процес (единен поток), правила за придвижване, BPM flowchart (Mermaid) и детайлна sequence диаграма (PlantUML).
3. **Задача 3 ([`architecture.drawio`](deliverables/03_architecture/architecture.drawio) + [`architecture.md`](deliverables/03_architecture/architecture.md))** — 7-зонова архитектура с две защитни стени, DMZ, приложен слой (API Gateway, Complaints Orchestrator, AI Copilot, IdP), data zone (PostgreSQL, Redis, Object Storage, Audit log) и интеграция с CBS/CRM.
4. **Задача 4 ([`project_plan.md`](deliverables/04_project_plan/project_plan.md) + [`product_backlog.csv`](deliverables/04_project_plan/product_backlog.csv))** — обосновка на Agile избора, 4-фазен roadmap, 20 User Stories разпределени в 6 спринта.

## За финалния печатен документ

Четирите markdown файла могат да се консолидират в единен Word/PDF документ със следната структура:

1. Заглавна страница
2. Увод (½ страница)
3. Проучване — от `research.md`
4. Сравнение на аналогичен процес — извадка от `research.md` Раздел 7 + роли от `process_and_sequence.md`
5. Sequence диаграма с обяснение — от `process_and_sequence.md` + експорт на PlantUML
6. Архитектура — от `architecture.md` + експорт на drawio
7. Проектен план — от `project_plan.md`
8. Заключение
9. Източници

## Как се рендерират диаграмите

- **PlantUML (`.puml`)** — [plantuml.com](https://www.plantuml.com/plantuml/uml/), или локално с `brew install plantuml && plantuml sequence_complaint.puml`
- **drawio (`.drawio`)** — [app.diagrams.net](https://app.diagrams.net/), Desktop drawio, или VS Code extension
- **Mermaid (inline в `.md`)** — GitHub / VS Code / всеки Markdown renderer с Mermaid поддръжка

## Лог на AI взаимодействията

Всички сесии с AI асистента са документирани в [`documentation/LLM/ai_usage_log.md`](documentation/LLM/ai_usage_log.md), с обосновка на решенията, pivot-ите и корекциите.
