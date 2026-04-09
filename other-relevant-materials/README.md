# Other Relevant Materials

Reference templates and examples provided by course instructors, used as a basis for developing course project deliverables.

---

## Product-backlog-template.xls

**Type:** Excel template

A product backlog template for Agile/Scrum project tracking. Contains the following sheets:

- **PRODUCT BACKLOG** — main sheet with columns: User Story ID, User Story, Estimate (size), Priority, Sprint, Task Owner, Estimated Effort (hours/days)
- **PROJECT DETAILS** — metadata fields: project number, project name, student names, date, version
- **DROPDOWN MENUS** — predefined values for Priority (1-5) and Sprint (1-6+) used as dropdowns in the backlog sheet
- **RESOURCES** — includes a burndown chart template with columns for Days, Goal, Done, Goal Velocity, and Remaining

**Used for:** Structuring the project's user stories, sprint planning, and tracking progress.

---

## Project Plan.pdf

**Type:** Single-page PDF (image-based)

An example project plan, likely in Gantt chart format. Serves as a visual reference for how to structure project timelines, milestones, and task dependencies.

**Used for:** Reference when building the project's own project plan/timeline.

---

## БА- Упражнение_v3_20260316.docx

**Type:** Word document (Exercise worksheet)

Business Analysis exercise (Exercise 1) — "Introduction to Business Analysis." Contains:

1. **Product Vision Board** — task to create a vision board for a mobile expense management application
2. **Sequence Diagrams** — two detailed diagram specifications:
   - **"Display customer accounts (active only)"** — interaction flow between BBM_USER, BBM, BBO_BE, and CORE_ACC for retrieving and displaying only active bank accounts
   - **"Request for new digital card"** — multi-system interaction flow covering BBM_USER requesting a digital debit card, with validation checks across CORE_BANKING, CARD_SYSTEM, and CARD_SYSTEM_MODULE_DIGICARD (includes conditional branching for eligibility and card limit checks)
3. **Glossary** — definitions for system acronyms (BBM, BBO_BE, CORE_BANKING, CARD_SYSTEM, etc.)

**Used for:** Implementing sequence diagrams and user flow analysis for the course project.

---

## Създаване на дигитален workflow за одобрение на кредитни сделки.docx

**Type:** Word document (Process description)

Describes a digital workflow for credit deal approval. The end-to-end process covers:

1. Client submits a credit request (paper form at branch or via internet banking)
2. If submitted at branch — Relationship Manager enters the application and scans/attaches supporting documents; if online — client attaches documents directly
3. Request goes to a Credit Risk Expert for review
4. Credit Risk Expert may request additional opinions from Legal or Regulatory Control departments
5. Credit Risk Expert prepares the request for the Credit Committee
6. Credit Committee approves or rejects the credit
7. Relationship Manager notifies the client of the decision
8. If approved — request moves to Credit Administration for contract preparation
9. Relationship Manager signs the contract with the client and forwards to Credit Administration
10. Credit Administration disburses the credit to the client's account

**Used for:** Reference example of a real-world banking workflow digitalization process, relevant to understanding how business processes are modeled and automated.
