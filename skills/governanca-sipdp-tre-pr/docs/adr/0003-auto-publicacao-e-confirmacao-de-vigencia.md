---
status: accepted
date: 2026-09-02
---

# Publicação automática de novas normas + critério de confirmação de vigência

Duas decisões de processo registradas juntas porque nasceram da mesma rodada de evolução
(2026-09-02): como o acervo cresce e quem confirma vigência.

## Decisão 1 — Critério de confirmação de vigência para páginas novas

Uma norma recém-adicionada por monitoramento nasce `não-confirmada`/`pendente` (convenção já
estabelecida). A promoção a `vigente`/`completa` exige, na ordem:

1. **Publicação oficial** (DJE-TRE-PR / DJE-TSE / DOU) — veículo, número, data e página; OU
2. **Página oficial individual** no compilado do tribunal, com texto integral acessível — vale
   como sustentação intermediária quando o DJE exato ainda não foi rastreado, registrando a
   lacuna de listagem quando aplicável.

Racional: a ADR 0002 diz que a verdade é a publicação oficial. Na prática, o portal do TRE-PR
mantém página individual com o texto integral e a referência ao DJE no rodapé — coletar o texto
já traz a citação DJE embutida. Caso real: a Res. 940/2024 não aparece na listagem compilada de
2024 (que mostra até 942/2024), mas a página individual funciona e o rodapé cita DJE-TRE-PR
nº 325, 07/11/2024, p. 11-24 — vigência sustentada pelo DJE, não pela listagem.

## Decisão 2 — Auto-publicação de novas normas pelo monitoramento semanal

O cron de monitoramento (segunda 08:00) passa a **publicar automaticamente** o que for
**adição de norma nova com texto integral coletado** — criando a página (`não-confirmada`/
`pendente`), atualizando index/log/relatório, rodando `sync_vault_to_build.py`, commitando,
tagueando e criando release no GitHub. **Revogações, alterações de status e decisões de
escopo continuam exigindo revisão humana** — o cron reporta e encerra, sem tocar no repo.

Racional: o valor do monitoramento é não depender de alguém lembrar de publicar; adição de
norma é baixo risco (nasce `não-confirmada` e a curadoria humana revisa depois, como já é a
convenção). Revogação é decisão jurídica demais para automação cega.

## Consequences

- O número de páginas `não-confirmada` pode crescer entre rodadas de curadoria humana — aceito
  por desenho (a camada curada é revisada por humano).
- O cron precisa de credencial GitHub válida no ambiente (gh autenticado) — se falhar, reporta
  erro e encerra sem meia-publicação.
- O release automático segue o fluxo `release_plugin.py` (bump patch + tag + release).
- A fronteira entre "norma nova" (publica) e "revogação/escopo" (reporta) é o ponto que exige
  julgamento do agente a cada rodada — documentada no prompt do cron.
