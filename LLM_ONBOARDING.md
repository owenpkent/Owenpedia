# LLM Onboarding

Quick reference for AI assistants working on this repository.

---

## Project Context

**Owenpedia** is a caregiver onboarding wiki for Owen Kent, who has muscular dystrophy and requires 24/7 care support. This repository contains:

- Daily care routines and procedures
- Medical equipment guides
- Household responsibilities
- Employment documentation
- Recipes and meal planning

The content is structured as a Wikipedia-style wiki with internal links between pages.

---

## About Owen (Project Owner)

I'm Owen — a lifelong wheelchair user with muscular dystrophy. A few things that shape how I work:

**Typing is difficult for me.** I rely heavily on AI coding assistants (Cursor, Windsurf, Claude) to write code and documentation. When interacting with me:

- **Offer choices as A, B, C options** — I can type a single letter instead of explaining my preference
- **Be proactive** — Make decisions and implement rather than asking for confirmation on every detail
- **Propose complete solutions** — Don't ask me to type out requirements; infer from context and iterate

**PowerShell is my preferred shell.** I work on Windows and use PowerShell for command-line tasks. **I strongly prefer single-line commands** using semicolons (`;`) to chain operations when possible for efficiency.

---

## Repository Structure

```
Owenpedia/
├── README.md                    # Wiki homepage
├── LLM_ONBOARDING.md           # This file
├── .gitignore                   # Excludes original .docx/.xlsx files
├── .gitattributes               # Line ending normalization
├── docs/
│   ├── daily-routines/          # Morning, evening, bedtime, night routines
│   ├── employment/              # Job description, employee handbook
│   ├── household/               # Chores, house manual
│   ├── medical/                 # Feeding, equipment, medications, catheter
│   ├── travel/                  # Packing checklists
│   └── recipes/                 # Meal ideas
└── scripts/
    ├── convert_files.py         # Converts .docx to .md, .xlsx to .csv
    └── organize_repo.py         # File organization utility
```

---

## Key Files

| File | Purpose |
|------|---------|
| `README.md` | Wiki homepage with navigation |
| `docs/daily-routines/morning-routine.md` | Most detailed care procedure |
| `docs/medical/feeding.md` | G-tube feeding guide |
| `docs/medical/supplies-reordering.md` | Supplier contacts and schedules |
| `docs/household/house-manual.md` | Emergency contacts, WiFi, etc. |

---

## Conventions

### Markdown Style
- Use relative links between wiki pages: `[Link Text](../folder/page.md)`
- Tables for structured data
- Checklists with `- [ ]` syntax
- Clear headings hierarchy (H1 for title, H2 for sections)

### File Naming
- Lowercase with hyphens: `morning-routine.md`
- Descriptive names matching content

### Content Guidelines
- Write for caregivers who may have no medical background
- Be specific about quantities, times, and sequences
- Include "See Also" sections for related pages

---

## Sensitive Information

This wiki contains:
- **Medical information** (insurance IDs, supplier accounts)
- **Contact information** (phone numbers, addresses)
- **House access** (WiFi password, door codes)

Handle with appropriate care. This repo should remain private or access-controlled.

---

## Common Tasks

### Adding a New Page
1. Create `.md` file in appropriate `docs/` subfolder
2. Add internal links to related pages
3. Add entry to `README.md` navigation table

### Updating Routines
- Keep step-by-step format
- Link to equipment/supply pages
- Update "See Also" sections

### Converting Source Documents
```powershell
python scripts/convert_files.py
```

---

## Integration

This repo follows [Constellation](./CONSTELLATION_INTEGRATION_GUIDE.md) conventions for cross-project visibility.

---

## Questions?

Reach out to Owen or infer from context and iterate.
