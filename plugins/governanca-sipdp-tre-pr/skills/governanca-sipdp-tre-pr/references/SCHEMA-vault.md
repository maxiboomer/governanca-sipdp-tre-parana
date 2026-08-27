# Schema do Vault Normativo TRE-PR / TSE / CNJ

## Camadas

- `raw/`: fontes integrais imutáveis. Nunca editar.
- `wiki/normas/`: uma página por instrumento normativo, com status e fonte.
- `wiki/concepts/`: sínteses temáticas e operacionais.
- `wiki/entities/`: órgãos, comitês, unidades e responsáveis.
- `wiki/inventarios/`: inventários e tabelas de cobertura.
- `wiki/_meta/`: changelogs, qualidade, mapa temático e pendências.

## Frontmatter obrigatório em páginas wiki

```yaml
---
title: "Título"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: fonte-normativa | concept | entity | inventory | metadata
status: vigente | revogada | alterada | não-confirmada | histórica | não-aplicável
status_verificacao: "Fonte e data da última verificação"
sources: [raw/arquivo.md]
tags: [vocabulário controlado]
---
```

Páginas de norma devem registrar também `fonte_publicacao`, quando disponível, e `data_publicacao`.

## Regras de vigência

- A publicação oficial (DJE-TRE-PR, DJE-TSE, DOU ou atos.cnj.jus.br) é a autoridade para vigência.
- O inventário e o nome do arquivo são apenas índices; não provam vigência.
- `não-confirmada` é obrigatório quando a situação não foi verificada oficialmente.
- Norma revogada permanece no vault quando tiver valor histórico, efeito residual ou explicar uma sucessora.
- Norma revogada sem valor analítico pode ser arquivada em `wiki/_archive/normas/`, sem apagar o `raw/`.

## Qualidade e curadoria

- `curadoria: completa | resumo | stub` identifica profundidade, não vigência.
- `escopo: central-si-pdp | apoio-governanca-ti | contextual | fora-escopo | duplicada` identifica utilidade.
- Toda norma curada deve apontar para a fonte bruta e, quando possível, para sucessoras/alteradoras.
- Sínteses de múltiplas fontes devem indicar as fontes usadas.
- Links Obsidian usam `[[wiki/...]]`.

## Convenções de manutenção

- Atualizar `index.md` e acrescentar entrada em `log.md` em toda alteração estrutural.
- Não alterar arquivos em `raw/`.
- Antes de afirmar vigência, conferir a publicação oficial.
- Duplicatas devem ter uma página canônica e um alias/redirecionamento preservando links antigos.
- Relatórios e changelogs não pertencem a `wiki/normas/`; ficam em `wiki/_meta/`.
