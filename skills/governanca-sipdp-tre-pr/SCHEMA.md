# Schema do Vault Normativo TRE-PR / TSE / CNJ

## Camadas

- `references/raw/`: fontes integrais imutáveis. Nunca editar. Todo raw deve ter frontmatter com `source_url` (quando aplicável) e `sha256` do corpo (detecção de drift em re-coleta).
- `references/normas/`: uma página por instrumento normativo, com status e fonte.
- `references/concepts/`: sínteses temáticas e operacionais.
- `references/entities/`: órgãos, comitês, unidades e responsáveis.
- `references/comparisons/`: comparações lado a lado de normas/temas relacionados (síntese compilada).
- `references/inventarios/`: inventários e tabelas de cobertura.
- `references/_meta/`: changelogs, qualidade, mapa temático e pendências.

## Frontmatter obrigatório em páginas wiki

```yaml
---
title: "Título"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: fonte-normativa | concept | entity | inventory | metadata
status: vigente | revogada | alterada | não-confirmada | histórica | não-aplicável
status_verificacao: "Fonte e data da última verificação"
sources: [references/raw/arquivo.md]
tags: [vocabulário controlado]
---
```

Páginas de norma devem registrar também `fonte_publicacao`, quando disponível, e `data_publicacao`.

## Regras de vigência

- A publicação oficial (DJE-TRE-PR, DJE-TSE, DOU ou atos.cnj.jus.br) é a autoridade para vigência.
- O inventário e o nome do arquivo são apenas índices; não provam vigência.
- `não-confirmada` é obrigatório quando a situação não foi verificada oficialmente.
- Norma revogada permanece no vault quando tiver valor histórico, efeito residual ou explicar uma sucessora.
- Norma revogada sem valor analítico pode ser arquivada em `references/_archive/normas/`, sem apagar o `references/raw/`.

## Qualidade e curadoria

- `curadoria: completa | resumo | stub` identifica profundidade, não vigência.
- `escopo: central-si-pdp | apoio-governanca-ti | contextual | fora-escopo | duplicada` identifica utilidade.
- `confidence: high | medium | low` (opcional) indica robustez das afirmações: `high` exige
  DJE/DOU nomeado no `status_verificacao`; `medium` = compilado oficial sem DJE rastreado;
  `low` = monitoramento sem confirmação. O lint sinaliza páginas `low` para revisão.
- `contested: true` (opcional) marca páginas com contradições não resolvidas — o lint as
  lista para revisão humana.
- Toda norma curada deve apontar para a fonte bruta e, quando possível, para sucessoras/alteradoras.
- Sínteses de múltiplas fontes devem indicar as fontes usadas (`sources:` e marcadores `^[...]`).
- Links Obsidian usam `[[references/...]]`.
- Páginas de comparação (`type: comparison`) seguem o mesmo frontmatter, com `status: não-aplicável`.

## Convenções de manutenção

- Atualizar `index.md` e acrescentar entrada em `log.md` em toda alteração estrutural.
- Não alterar arquivos em `references/raw/`.
- Antes de afirmar vigência, conferir a publicação oficial.
- Duplicatas devem ter uma página canônica e um alias/redirecionamento preservando links antigos.
- Relatórios e changelogs não pertencem a `references/normas/`; ficam em `references/_meta/`.
