---
title: "Relatório de Monitoramento Normativo"
created: 2026-08-26
updated: 2026-08-26
type: metadata
status: não-aplicável
curadoria: completa
escopo: contextual
tags: [monitoramento, auditoria, vigencia]
---

# Relatório de Monitoramento Normativo

Relatório **report-only**: registra o que foi verificado nas fontes oficiais e o que
decorre disso. Nada aqui altera o vault automaticamente.

## Rodada 2026-08-26

### Fontes verificadas (via serviço de extração web, não urllib)

| Fonte | URL | Status |
|---|---|---|
| TRE-PR Resoluções 2025 | `.../resolucoes-tre-pr/2025` | Acessível |
| TRE-PR Resoluções 2026 | `.../resolucoes-tre-pr/2026` | Acessível |
| TRE-PR INs 2025 | `.../instrucoes-normativas-tre-pr/2025` | Acessível |
| TRE-PR Normas Técnicas SECTI 2026 | `.../normas-tecnicas-da-secti/2026` | Acessível |
| TSE / CNJ (detalhe) | `atos.cnj.jus.br`, `tse.jus.br` | Bloqueado a urllib; usar extração |

> **Nota de canal:** o acesso direto via `urllib`/curl é bloqueado com HTTP 403 pelos portais.
> O monitoramento operacional usa o serviço de extração web (que resolve como navegador). O
> script `monitor_normas.py` está mantido como referência de fontes, mas o acionamento real é
> sob demanda / via extração.

### Normas SI/PDP-relevantes publicadas e ausentes do vault (detectadas)

O diff das listagens oficiais de 2025/2026 contra o vault identificou **6 normas relevantes**
para segurança da informação / proteção de dados / governança de TI que ainda não estavam no
acervo:

| Norma | Assunto | Ação |
|---|---|---|
| Res. TRE-PR 970/2026 | Política de Gestão da Inovação | **Adicionada** ao vault |
| Res. TRE-PR 979/2026 | Captação/registro audiovisual em atos processuais (LGPD) | **Adicionada** ao vault |
| Res. TRE-PR 983/2026 | Altera Res. 852/2020 (mensagens instantâneas) | **Adicionada** ao vault |
| Res. TRE-PR 946/2025 | Política Antirretaliação | **Adicionada** ao vault |
| Res. TRE-PR 958/2025 | Utilização do PJe | **Adicionada** ao vault |
| NT SECTI 002/2026 | Metodologia de Desenvolvimento de Sistemas (MDS) | Adicionada; texto integral pendente |

### Revogações indiretas detectadas

- **Res. TRE-PR 979/2026 revoga a Res. TRE-PR 615/2012** (captação audiovisual anterior).
- **Res. TRE-PR 958/2025 revoga a Res. TRE-PR 774/2017** (PJe anterior).
- **Res. TRE-PR 970/2026 teve o art. 8º (atribuições do CGER) revogado pela Res. 980/2026.**

### Fora de escopo (não adicionadas)

As demais normas de 2025/2026 não presentes no vault são de tema administrativo/eleitoral sem
relação com SI/PDP/governança de TI (denominação de espaços, eleições suplementares, bandeira,
avaliação de estágio probatório, plebiscitos, comissões de auditoria da votação, planos de
obras, comunicação social). Ficam fora da camada de curadoria.

## Próximas rodadas

- Reconferir as listagens de 2026 (Resoluções/INs/NTs) periodicamente para novas publicações.
- Coletar o texto integral da NT SECTI 002/2026 (MDS).
- Reavaliar TSE/CNJ quando o acesso por extração permitir.
