# Gemini Presentation Maker — Paste-Ready Prompt

> **Как се използва:** Отворете Google Gemini (gemini.google.com) в режим за генериране на презентация (или Canvas / Slides generator). Копирайте **всичко** под разделителя `---BEGIN PROMPT---` и го пейстнете. Gemini ще изгради 19-слайдов Google Slides deck в стилистиката на UniCredit Bulbank. След генерацията ръчно вмъкнете актуалните скрийншоти от `deliverables/01_research/images/` и експортите на `sequence_complaint.puml` + `architecture.drawio` на съответните слайдове (Gemini не може да чете локални файлове).

> **Защо подробен prompt:** Gemini е добър генератор, но без строга спецификация пропуска ключови акценти (брандинг, правилен ред на слайдовете, точно съдържание). Този prompt елиминира „drift" и дава на Gemini строг шаблон за всеки от 19-те слайда.

---BEGIN PROMPT---

# Build a 19-slide Google Slides deck: „Дигитализация на процеса по жалби в UniCredit Bulbank"

You are building a **university course-work presentation** in Bulgarian for the discipline „Дигитализация в банкирането" (Technical University — Sofia). The deck will be defended in **7 minutes by 3 presenters** (≈2:20 each). Generate a **Google Slides-compatible deck with 19 slides**, following the brand guide, layout library, and per-slide specifications below **literally**. Do not invent content outside this spec. Do not expand the slide count.

## 1. Brand & Style Guide

### Colors (use these exact hex values)
- **Primary — UniCredit Red:** `#E30613` (Pantone 485 C). Use for: title bars, section dividers, key stat highlights, active elements, data emphasis.
- **Secondary — Charcoal Black:** `#1A1A1A`. Use for: body text.
- **Neutral — Off-White:** `#FAFAFA`. Use for: slide background (preferred over pure white — gentler on screen).
- **Accent — Light Gray:** `#EEEEEE`. Use for: table header backgrounds, card surfaces, subtle dividers.
- **Warning/Alert:** `#D32F2F` (slightly softer than primary). Use sparingly for warning badges if needed.
- **Success:** `#2E7D32`. Use sparingly for positive check marks in comparison tables.

### Typography
- **Headings:** Sans-serif, bold — use **Inter**, **Roboto**, or fallback **Arial**. Never Times New Roman for slides.
- **Body:** Same sans-serif family, regular weight.
- **Font sizes:**
  - Slide title: 32–36 pt, bold, color `#1A1A1A` (or `#FFFFFF` on red bars).
  - Section headers within slide: 20–24 pt, bold.
  - Body text: 16–18 pt.
  - Caption / footnote: 12 pt, color `#666666`.
- **Line spacing:** 1.2× for body, 1.0× for titles.

### Tone & register
- Bulgarian throughout. Formal register — „Настоящата презентация…", „Предложеният процес…", not colloquial.
- Avoid exclamation marks. Avoid emojis. No decorative clipart.
- Numbers and percentages in bold to draw the eye.
- Every regulatory citation in the exact form: **ЗПУПС чл. 174, ал. 1**; **EBA/GL/2015/18**; **GDPR чл. 5**. Never paraphrase to non-standard names.

### Visual design principles
- **Generous whitespace.** No slide should feel crowded. If a slide needs more than 5 bullets, split it.
- **One big idea per slide.** Title should make the point; body supports.
- **Consistency of position:** page number in the bottom-right corner (size 10pt, color `#999999`), format `{n} / 19`. Slide title always at the top-left, 36pt bold. Leave a 4pt-tall `#E30613` bar under the title on content slides.
- **Images respect brand:** if Gemini generates placeholder images, they should be minimal, flat, with a thin `#E30613` border if bordered at all. No drop shadows, no 3D effects.

## 2. Layout Library (use these exact 5 layouts)

| Layout | Use for | Description |
|---|---|---|
| **L1 — Title Page** | Slide 1 | Full-bleed off-white background with a solid `#E30613` vertical bar on the left 10% of the slide. University name + faculty + course + topic + team + date, all left-aligned in the right 90%. No visuals. |
| **L2 — Section Divider** | Slides 3, 11, 15, 17 | Full-bleed `#E30613` background. Giant white section number (e.g., „01") in the left third, 180pt, ultra-bold. Section title on the right in white, 40pt bold. |
| **L3 — Content + Bullets** | Most content slides | Off-white bg. Title top-left with 4pt red bar under it. 3–5 bullets in the left 55%, an optional visual/image placeholder or callout box in the right 45%. Page number bottom-right. |
| **L4 — Full Visual** | Slides 5, 13, 14, 16 | Off-white bg. Small title top-left with red bar. The rest of the slide is reserved for a single large visual (diagram, screenshot collage). A 1-line caption below the visual. |
| **L5 — Comparison Table** | Slides 6, 18 | Off-white bg. Title top-left with red bar. Full-width table occupying 75% of slide height, with header row in `#EEEEEE` bg + bold text, accent column (UCB / our solution) in `#FFE5E7` tint (very light red). |

## 3. Slide-by-Slide Specification

> **Rule:** For every slide, build exactly what's specified. If a field says `[visual placeholder: description]`, insert a placeholder box with that text — the user will drop in the real image later.

---

### Slide 1 — Title Page · Layout L1
- **Left bar:** solid `#E30613`, 10% slide width.
- **Right content (left-aligned, vertical-centered):**
  - `ТЕХНИЧЕСКИ УНИВЕРСИТЕТ — СОФИЯ` (13pt, bold, `#666666`)
  - `Факултет Компютърни системи и технологии` (11pt, `#666666`)
  - Spacer
  - `КУРСОВА РАБОТА` (44pt, bold, `#1A1A1A`)
  - Spacer
  - `дисциплина: „Дигитализация в банкирането"` (16pt, `#1A1A1A`)
  - `тема: „Дигитализация на процеса по жалби` (24pt, bold, `#E30613`)
  - `в UniCredit Bulbank"` (24pt, bold, `#E30613`)
  - Spacer
  - `Изготвили (III курс, специалност КСИ):` (12pt)
  - `[Име 1] · Фак. № [номер]` (12pt)
  - `[Име 2] · Фак. № [номер]` (12pt)
  - `[Име 3] · Фак. № [номер]` (12pt)
  - Spacer
  - `София, 2026` (12pt, `#666666`)

---

### Slide 2 — Agenda · Layout L3
- **Title:** „Съдържание"
- **Content (numbered list, large — 20pt):**
  1. **Проучване** — процес по жалби в UCB, DSK, ОББ; международен бенчмарк; регулаторна рамка
  2. **Продуктова визия** — кой, защо, какво, как измерваме успех
  3. **Процес и дизайн** — роли, to-be процес, sequence диаграма
  4. **Архитектура** — мрежови сегменти, технологичен стек, защитни стени
  5. **Проектен план** — Agile план, 4 фази, Backlog highlights
- **Footer note (bottom, 11pt grey):** „Презентатори: П1 (слайдове 1–9) · П2 (10–14) · П3 (15–19)"

---

### Slide 3 — Section Divider „01 Проучване" · Layout L2
- **Left:** giant `01` in white, 180pt, ultra-bold.
- **Right:** `Проучване` (40pt white bold), subtitle below in white 20pt regular: „Процес по жалби в трите български банки + международен бенчмарк".

---

### Slide 4 — Ключови тенденции · Layout L3
- **Title:** „Ежедневното банкиране е дигитално, но жалбите — не"
- **Content (3 bullets + 1 big stat):**
  - **В UCB над 97% от плащанията се правят през дигитални канали** (UCB / Global Finance, 2024)
  - Жалбите остават хибриден процес: уеб + клон + имейл
  - Регулаторите вече изискват регистрация, SLA, одитен лог — лесно в дигитален процес
- **Right-side callout box (big stat):**
  - Huge number `97%` in `#E30613`, 96pt, bold
  - Below in 14pt: „от плащанията в UCB са дигитални"
  - Small `vs.` separator
  - Huge number `0%` in `#1A1A1A`, 96pt, bold
  - Below in 14pt: „от жалби с PII могат да се подадат онлайн без КЕП"

---

### Slide 5 — Research evidence: 4-bank screenshot collage · Layout L4
- **Title:** „Как изглежда процесът днес"
- **Visual layout:** 2×2 grid of screenshots, each labeled with bank name + one-line takeaway.
  - **Top-left:** `[image: deliverables/01_research/images/ucb_form_top.png]` · label „**UCB** — web form; изисква КЕП при PII"
  - **Top-right:** `[image: deliverables/01_research/images/dsk_email_reference_number.png]` · label „**DSK** — 2 имейла, референтен номер, 3 дни SLA"
  - **Bottom-left:** `[image: deliverables/01_research/images/ubb_confirmation.png]` · label „**ОББ** — 45-дневен обявен срок, без референтен номер"
  - **Bottom-right:** `[image: deliverables/01_research/images/revolut_complaint_response.png]` · label „**Revolut** — in-app AI chat, ескалация с една стъпка"
- **Caption below:** „Тествано от първо лице на 2026-04-09" (11pt, italic).

---

### Slide 6 — Comparison table: 3 банки + Revolut · Layout L5
- **Title:** „Сравнение: къде е пропускът?"
- **Table (6 rows × 5 columns):**

| Аспект | UniCredit Bulbank | DSK Bank | ОББ | Revolut |
|---|---|---|---|---|
| In-app подаване | ✗ Не | ✗ Не | ✗ Не | ✓ Да |
| Референтен номер | ✗ Не | ✓ Да | ✗ Не | ✓ Да |
| Имейл потвърждение | ✗ Не | ✓ 2 имейла | ✗ Не | ✓ Да |
| AI триажна оценка | ✗ Не | ✗ Не | ✗ Не | ✓ Да |
| Обявен срок | 3 / 15 дни | 3 работни дни | **45 дни** | 15 работни дни |
| КЕП при PII | **Изисква се** | Не | Не | Не |

- **Styling:** Header row `#EEEEEE` background, bold text. „UCB" column shaded `#FFE5E7` (very light red) because it's our client. „Изисква се" and „45 дни" in bold red `#E30613` to highlight the worst outcomes. ✓ in `#2E7D32`, ✗ in `#999999`.

---

### Slide 7 — Revolut benchmark detail · Layout L3
- **Title:** „Международен бенчмарк — Revolut"
- **Left bullets:**
  - Входната точка е **вградена директно в приложението** (Profile → Help)
  - AI chat разпознава намерение **в реално време**: *„You have the right to raise a formal complaint. Would you like me to connect you with a customer support agent?"*
  - **Една стъпка** до ескалация до човек
  - Не изисква КЕП — автентикацията в приложението е достатъчна
- **Right visual:** `[image: deliverables/01_research/images/revolut_complaint_response.png]`
- **Bottom bar (centered, 16pt):** „Нулево триене на входа + AI асистиране на специалиста"

---

### Slide 8 — Асиметрия: къде е пропускът? · Layout L3
- **Title:** „Парадоксът на UCB"
- **Content (grouped in 2 columns):**
  - **Left column (red header „Какво вече работи"):**
    - 97% дигитални плащания
    - Онлайн кредити с електронен подпис
    - Пълно дистанционно онбординг
  - **Right column (black header „Какво не работи"):**
    - Жалби с PII → изискват КЕП или клон
    - Ежегодно: хиляди клиенти в неприятен offline loop
    - Bulbank Mobile няма видимост на жалбите
- **Bottom callout (full-width, `#E30613` bg, white text, 20pt):** „В Bulbank Mobile клиентът е **вече автентикиран** — правната бариера автоматично отпада"

---

### Slide 9 — Регулаторна рамка · Layout L5
- **Title:** „Регулаторна рамка"
- **Table (3 rows × 2 columns):**

| Разпоредба | Какво изисква |
|---|---|
| **ЗПУПС чл. 174, ал. 1** | Доставчикът на платежни услуги отговаря в рамките на **15 работни дни**. |
| **ЗПУПС чл. 174, ал. 4** | При изключителни обстоятелства — удължаване до **35 работни дни**, с междинно уведомяване. Транспонира PSD2 чл. 101. |
| **EBA/GL/2015/18** | Задължителна регистрация, функция за управление, регулярно отчитане. |

- **Bottom box (off-white bg, red left border 4pt):** „**ЗА ПРОЕКТА:** Предложеният in-app процес връща отговор **под 3 работни дни** — значително под регулаторния таван. Append-only audit log директно покрива EBA/GL/2015/18 за регистрация и отчитане."

---

### Slide 10 — Product Vision Board · Layout L4 (custom)
> **IMPORTANT:** This is a product vision board. Render as a single visual composed of **1 top banner (vision statement) + 4 quadrants**, all on one slide. Each quadrant is a `#FAFAFA` card with a thin `#E30613` top border (4pt) and an icon in `#E30613`.

- **Title:** „Продуктова визия"
- **Top banner (full width, `#E30613` bg, white text, centered, 24pt bold):**
  „**UniCredit Bulbank — първата българска банка с напълно дистанционен, in-app жизнен цикъл на жалбата**"
- **Quadrants (2×2 grid below the banner):**

  **Q1 — ЦЕЛЕВИ ПОТРЕБИТЕЛИ (icon: users)**
  - Физически лица — клиенти на UCB с активен Bulbank Mobile / Online
  - Специалисти „Централизирано управление на оплакванията"
  - Ръководители (supervisors), одобряващи монетарни действия

  **Q2 — НУЖДИ / ПРОБЛЕМИ (icon: alert)**
  - Жалбите с PII изискват КЕП или посещение в клон
  - Няма референтен номер, нито видимост на статус при UCB
  - Специалистите губят време да събират контекст от 3–4 системи
  - Регулаторното отчитане е ръчно и податливо на грешки

  **Q3 — ПРОДУКТ (icon: box)**
  - In-app модул „Жалби" в Bulbank Mobile / Online
  - AI Копилот (self-hosted) — асемблира контекст и предлага чернова
  - Append-only audit log за регулаторна проследимост
  - Supervisor approval gate за всяко монетарно действие

  **Q4 — БИЗНЕС ЦЕЛИ / УСПЕХ (icon: target)**
  - **<3 работни дни** среден SLA (спрямо таван 15 дни по ЗПУПС)
  - **100%** в-app обработка (0% посещения в клон за жалби)
  - **-50%** време за разследване на специалист (чрез AI контекст)
  - **0** breach на регулаторен срок в първата година

---

### Slide 11 — Section Divider „02 Процес и дизайн" · Layout L2
- Giant `02` + „Процес и дизайн" · subtitle „Роли, to-be процес, sequence диаграма"

---

### Slide 12 — To-Be процес: единен поток + AI Копилот · Layout L3
- **Title:** „Нашият подход — единен процес с AI Копилот"
- **Left bullets:**
  - **Единен поток** — всяка жалба минава през един и същи път
  - **AI Копилотът** — помощник на специалиста: асемблира контекст и предлага чернова
  - **Регулаторно правило (EBA/GL/2015/18):** AI не взема решения — винаги има човек между предложението и клиента
  - **Монетарни действия** изискват допълнително одобрение от ръководител
- **Right visual (flow diagram, horizontally):**
  `Клиент → Bulbank Mobile → Банков сървър → (CBS + AI Копилот) → Специалист → (Ръководител при монетарно) → Клиент`
  Use arrows between boxes. Boxes in `#FAFAFA` with `#E30613` 2pt border. The „AI Копилот" box should be shaded `#FFE5E7`.

---

### Slide 13 — BPM процесна диаграма (Mermaid) · Layout L4
- **Title:** „BPM процесна диаграма"
- **Visual:** `[image placeholder: export of Mermaid flowchart from process_and_sequence.md §5. The flow: Login → Open complaints module → New complaint → Registration → Push notification → Route to specialist → AI Copilot context → Specialist decision → (Monetary? → Supervisor approval → CBS execution) → Delivery → (Accept? → Close | Dispute → Escalate → Final decision → Close)]`
- **Caption:** „Клиентска перспектива — 13 стъпки, 2 decision points (monetary, accept/dispute)"

---

### Slide 14 — Sequence диаграма (PlantUML) · Layout L4
- **Title:** „Sequence диаграма — 5 етапа"
- **Visual:** `[image placeholder: export of sequence_complaint.puml as PNG/SVG. Actors horizontally: Клиент → Приложение → Банков сървър → CBS → AI Копилот → Специалист → Ръководител]`
- **Caption bullets below visual (small, 12pt, 3 items in a row):**
  - Етапи: иницииране → регистрация → разследване → решение → обратна връзка
  - Alt-клонове: монетарно действие (одобрение от ръководител)
  - Alt-клон: оспорване от клиента (ескалация)

---

### Slide 15 — Section Divider „03 Архитектура" · Layout L2
- Giant `03` + „Архитектура" · subtitle „Мрежови сегменти, технологичен стек, защитни стени"

---

### Slide 16 — Архитектура · Layout L4
- **Title:** „Мрежови сегменти + 3 защитни стени"
- **Visual:** `[image placeholder: export of architecture.drawio as PNG/SVG. Shows: Internet → CheckPoint perimeter FW → DMZ (Reverse Proxy, NGINX+ModSecurity WAF pair, Web Proxy) → Internal FW → App NW Segment (Flex Cube CBS, Internal LB, Complaints backend HA pair, AI Copilot) → Internal FW → DB NW Segment (ComplaintsDB PostgreSQL, ObjectStore MinIO)]`
- **Right sidebar (narrow column, 12pt bullets):**
  - **Perimeter:** CheckPoint FW (443 only)
  - **DMZ:** NGINX + ModSecurity (RHEL 9, HA pair)
  - **App:** JBoss EAP 8, Spring Boot, JRE 21 (HA pair)
  - **AI:** Python 3.12 FastAPI, self-hosted — PII не напуска банката
  - **Data:** PostgreSQL 16 + MinIO (S3 object-lock за audit)
  - **CBS:** Oracle Flex Cube (WebLogic 12) — mTLS 443

---

### Slide 17 — Section Divider „04 Проектен план" · Layout L2
- Giant `04` + „Проектен план" · subtitle „Agile план, 4 фази, Backlog highlights"

---

### Slide 18 — Agile план + timeline · Layout L3 (modified)
- **Title:** „4 фази, 6 спринта, 12 седмици"
- **Left: reasoning bullets (16pt):**
  - **Защо Agile:** техническият риск е в интеграциите с CBS и автентикацията, не в кода
  - **Regulatory как** се уточнява итеративно с compliance (Sprint Review на всеки 2 седмици)
  - **Обхватът е преорганизируем** без пренаписване на договор
- **Right: horizontal Gantt-style bar chart (5 rows stacked, each bar `#E30613` with label):**
  - `Фаза 1 — Техн. ядро ████ (Спринт 1)` — CMP-001 до 005 (spikes, UX прототип)
  - `Фаза 2 — Клиентска пътека ████████ (Спринт 2–3)` — CMP-006 до 011
  - `Фаза 3 — Специалист + AI ████████ (Спринт 4–5)` — CMP-012 до 017
  - `Фаза 4 — Регулат. отчитане ████ (Спринт 6)` — CMP-018 до 020
  - `Hyper-care ██ (Седмица 13+)` — monitoring, corrections
- **Bottom strip (small stats in 3 red badges):**
  - **20** User Stories · **6** спринта · **8** души (Mobile×2, Backend×2, Integration, AI, PO/UX, Architect)

---

### Slide 19 — Заключение · Layout L3
- **Title:** „Заключение"
- **Content (4 compact bullets, 18pt):**
  - **Жалбата става 100% дигитална** — без клон, без КЕП, без отделен уеб формуляр
  - **Запазваме обявения 3-дневен SLA на UCB**, но го правим **проследим** — референтен номер, in-app статус, push нотификации
  - **Напълно под регулаторния таван** от 15 работни дни по ЗПУПС чл. 174 ал. 1
  - UniCredit Bulbank може да се позиционира като **първата българска банка с напълно дистанционен жизнен цикъл на жалбата**
- **Bottom-right callout (red, white text, 24pt bold):** „Благодарим за вниманието · Въпроси?"

## 4. Speaker Notes (add as notes below each slide)

For each slide, add speaker notes in Bulgarian **in the slide's notes area** (not on the slide itself). Keep each note to 2–4 sentences — this is what the presenter reads during defense. Match the 7-min constraint: roughly 20–30 seconds of speaking per slide.

- Slides 1–9 → Presenter 1
- Slides 10–14 → Presenter 2
- Slides 15–19 → Presenter 3

Base the speaker notes on the content of each slide. On transition slides (3, 11, 15, 17), the speaker notes should include a 1-sentence handoff („Моят колега ще продължи с…").

## 5. Final Delivery Checklist (include as a last hidden note, not a slide)

- [ ] 19 slides total, in specified order
- [ ] UniCredit Red `#E30613` applied consistently (title bars, dividers, callouts)
- [ ] Off-white `#FAFAFA` background on all content slides (not pure white)
- [ ] Page numbers in format `{n} / 19` bottom-right on all slides except Section Dividers (Layout L2)
- [ ] Image placeholders on slides 5, 7, 13, 14, 16 (user will replace with actual exports)
- [ ] Speaker notes in Bulgarian on every slide
- [ ] Team names and faculty numbers left as `[Име 1/2/3]` and `[номер]` placeholders
- [ ] No Times New Roman anywhere (sans-serif throughout)
- [ ] No emojis, no clip art, no decorative elements

---END PROMPT---

## What to do after Gemini generates the deck

1. **Export the drawio diagram as PNG** — open `deliverables/03_architecture/architecture.drawio` in diagrams.net, File → Export as → PNG (2× scale for crisp render). Insert on slide 16.
2. **Render the PlantUML sequence diagram** — paste contents of `deliverables/02_process/sequence_complaint.puml` into [plantuml.com](https://www.plantuml.com/plantuml/uml/) and download the PNG. Insert on slide 14.
3. **Render the Mermaid BPM flowchart** — copy the `mermaid` block from `deliverables/02_process/process_and_sequence.md` §5 into [mermaid.live](https://mermaid.live/), export as PNG. Insert on slide 13.
4. **Insert the 4 research screenshots** on slide 5 from `deliverables/01_research/images/`:
   - `ucb_form_top.png`, `dsk_email_reference_number.png`, `ubb_confirmation.png`, `revolut_complaint_response.png`.
5. **Insert the Revolut detail screenshot** on slide 7 from `deliverables/01_research/images/revolut_complaint_response.png`.
6. **Fill in team names** on slide 1.
7. **Rehearse timing** — aim for 20–25 sec per content slide, 10 sec per divider. Total budget: 7 minutes.
