
## [2026-08-31] update | Fechamento de pendências + evolução da skill
- **NT SECTI 002/2026 (MDS)**: texto integral coletado (DJE-TRE-PR nº 052, 23/03/2026, p. 08-09) em `raw/tre-pr-nt-secti-002-2026-mds.md`; página promovida a `vigente`/`completa`.
- **Portaria DG 124/2026 (CETI)**: curadoria concluída (`vigente`/`completa`), confirmada no compilado oficial + DJE-TRE-PR nº 050, 19/03/2026, p. 11-12.
- **IN TRE-PR 001/2026 (AcompVot)**: decisão de escopo registrada — mantida FORA do acervo (tecnologia eleitoral operacional, sem teor SI/PDP); pendência de revisão humana encerrada.
- `sync_vault_to_build.py` corrigido para incluir `raw/` e `wiki/raw/` (antes, textos integrais novos não chegavam ao `references/raw/` do repo).
- SKILL.md atualizado: 174→176 páginas; mapa rápido ganhou Res. 940/2024 e IN 004/2025; aviso da NT 002/2026 atualizado.
- index.md: estatísticas corrigidas (176 normas, 8 entities, 13 concepts, 3 inventários, 166 raws).

## [2026-08-31] update | Inclusão de normas ausentes detectadas em verificação manual
- Identificada a **Resolução TRE-PR 940/2024** (Código de Ética e Integridade) — vigente no portal, mas sem página curada no vault (apenas citada como `CONSIDERANDO` na IN 004/2025).
- Identificada a **Instrução Normativa TRE-PR 004/2025** (Gestão de Identidade e Controle de Acesso Lógico/Físico) — vigente no portal, mas sem página curada no vault (apenas em `raw/`).
- Criadas as páginas curadas:
  - `wiki/normas/tre-pr-resolucao-940-2024.md` (status: `não-confirmada`, curadoria: `pendente`)
  - `wiki/normas/tre-pr-in-instrucao-normativa-004-de-28-de-maio-de-2025.md` (status: `não-confirmada`, curadoria: `pendente`)
- Salvo o texto integral da Res. 940/2024 em `raw/tre-pr-resolucao-940-2024.md`.
- Atualizados `index.md` (seção "Normas (novas)") e `log.md`.
- Observação: a Res. 940/2024 não aparece na listagem compilada de 2024 do portal (que mostra apenas até 942/2024), embora a página individual funcione — possível desordem de indexação ou retificação não-refletida na sumarificação. Norma confirmada vigente via acesso direto à página.

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
