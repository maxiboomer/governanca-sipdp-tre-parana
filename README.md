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
SKILL.md                  # entrada da skill
references/index.md       # catálogo completo (194 páginas)
references/normas/        # página curada por norma (vigência, prazos, competências)
references/concepts/      # LGPD, continuidade, monitoramento SECTI...
references/entities/      # CGSI/PDP, ETIR, ANPD, DPO, SECTI...
references/inventarios/   # tabelas de vigência TRE-PR/TSE e CNJ
references/sources/       # sínteses por tipo de norma
references/raw/           # 154 textos integrais das normas (imutáveis)
```

Cobertura: PSI nacional/local, LGPD/PDP, governança de TI e IA, normas técnicas
SECTI, INs DG, portarias administrativas, resoluções TSE/TRE-PR/CNJ, LAI,
continuidade de negócios — acervo completo de normas do TRE-PR (2016–2026).

Fontes: normas publicadas no portal do TRE-PR, TSE e CNJ. As páginas curadas incluem data de atualização; verifique sempre a vigência antes de citar em documento oficial.
