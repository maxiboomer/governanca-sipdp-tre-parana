# governanca-sipdp-tre-pr

Skill de conhecimento (formato compatível com [Claude Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)) sobre **Governança de Segurança da Informação e Proteção de Dados Pessoais no TRE-PR e na Justiça Eleitoral**.

## Conteúdo

- **PSI nacional** — Res. TSE 23.763/2026 (e histórico das revogadas)
- **PSI local** — Res. TRE-PR 974/2026
- **LGPD/PDP** — fundamentos, framework documental, fases 1–2, maturidade, IA & LGPD, PGPPDP TSE 23.650/2021
- **Governança** — comitês (CGIA, comitê de crises cibernéticas 962/2025), CGSI/PDP (Port. DG 086/2026), Encarregado/DPO (Port. 247/2021), ETIR, CSI, SECTI
- **Continuidade** — PGCN Port. TRE-PR 302/2025 e Protocolo Socioambiental 056/2026
- **Prazos normativos consolidados** e inventário de vigências
- **Textos integrais** das normas-chave em `references/raw/`

## Uso

Instale como skill do Claude (web/desktop) ou copie para `~/.claude/skills/`.
Para agentes Hermes: copie a pasta para `~/.hermes/skills/`.

## Estrutura

```
SKILL.md              # entrada da skill
references/index.md   # catálogo
references/*.md       # páginas curadas por norma/conceito/entidade
references/raw/       # textos integrais imutáveis
```

Fontes: normas publicadas no portal do TRE-PR, TSE e CNJ. As páginas curadas incluem data de atualização; verifique sempre a vigência antes de citar em documento oficial.
