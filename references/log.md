
## [2026-08-26] update | Reconciliação e correção do fluxo de curadoria
- Identificado que a curadoria desta sessão havia sido gravada apenas no build (references/), não no vault (fonte da verdade).
- Portadas 159 páginas curadas do build de volta ao vault; raw/ preservado. Vault e build agora sincronizados (0 divergências).
- Corrigidos 96 wikilinks com prefixo `references/` incorreto (quebravam o vault).
- lint_vault.py corrigido: `curadoria` agora vem do frontmatter (fonte única), não de heurística de texto; adicionado check de prefixo `references/`.
- Vault: 206 páginas, 0 stubs, 0 links quebrados, 0 campos ausentes, 0 prefixo errado.

## [2026-08-26] update | Monitoramento normativo — 1ª rodada
- Identificadas e adicionadas ao vault 6 normas SI/PDP-relevantes publicadas em 2025/2026 que estavam ausentes: Res. TRE-PR 970/2026 (inovação), 979/2026 (captação audiovisual/LGPD), 983/2026 (altera 852/2020), 946/2025 (antirretaliação), 958/2025 (PJe) e NT SECTI 002/2026 (MDS, texto pendente).
- Revogações indiretas detectadas: 979/2026 revoga 615/2012; 958/2025 revoga 774/2017; art. 8º da 970/2026 revogado pela 980/2026.
- Criado wiki/_meta/relatorio-monitoramento.md (report-only) e atualizado monitor_normas.py (canal web, não urllib).
- lint_vault.py: index.md e log.md excluídos do check de campos obrigatórios (arquivos administrativos).
