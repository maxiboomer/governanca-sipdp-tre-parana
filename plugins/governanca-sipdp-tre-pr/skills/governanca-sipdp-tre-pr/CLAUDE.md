# LLM Wiki — Schema & Conventions

This directory is an Obsidian vault and a personal knowledge base following the pattern in the llmm-wiki manifesto. This file is the concrete schema: how *this* wiki is organized and how the agent should operate.

## Directory layout
```
llm-wiki/
├── raw/                  Immutable source documents (articles, PDFs, notes, transcripts)
├── wiki/
│   ├── entities/         Pages for people, organizations, products, tools
│   ├── concepts/         Pages for ideas, themes, techniques, topics
│   ├── normas/           Domain-specific: one page per legal/regulatory instrument
│   └── inventarios/      Domain-specific: raw consolidated tables
├── index.md              Catalog of every wiki page
└── log.md                Append-only chronological record
```

## Page conventions
- Filenames: `kebab-case.md`, matching the page title
- Every page starts with YAML frontmatter
- Use `[[wiki-links]]` (Obsidian-style) for cross-references
- Cite the originating source page when claims come from specific documents

## Operations

### Ingest
1. Read the new source in `raw/`
2. Discuss key takeaways with the human
3. Write/update `wiki/sources/<name>.md`
4. Update every `wiki/entities/` and `wiki/concepts/` page
5. Update `index.md` for anything created or changed
6. Append to `log.md`

### Query
1. Read `index.md` first to find candidate pages
2. Drill into the relevant wiki pages
3. Synthesize an answer with citations to `[[pages]]`
4. Offer to file substantial answers back into the wiki
5. Append to `log.md`

## Working with this vault
- Vault path: `/c/Users/CASA/llmwiki/llm-wiki/`
- This is a knowledge base for Brazilian electoral IT security, LGPD compliance, and governance