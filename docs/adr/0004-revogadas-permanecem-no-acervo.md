---
status: accepted
date: 2026-09-02
---

# Revogadas permanecem no acervo (divergência consciente com a mentalidade llm-wiki)

A mentalidade llm-wiki (skill `research/llm-wiki`) sugere arquivar em `_archive/` páginas
totalmente superadas. Este vault mantém, por decisão registrada, as normas `revogada` e
`histórica` **no próprio diretório `wiki/normas/`**, sinalizadas pelo campo `status`.

## Contexto

O acervo é de consulta normativa institucional (TRE-PR/TSE/CNJ). Normas revogadas têm valor
de **histórico ativo**: respondem "o que valia antes", explicam sucessoras, fundamentam
análises de adequação (ex.: a PSI antiga 23.644/2021 explica o descompasso da PSI local
974/2026). A skill já instrui que "normas revogadas permanecem como histórico, sinalizadas".

## Decisão

- **Não** mover revogadas/históricas para `_archive/` neste momento.
- Manter a sinalização por `status: revogada | histórica` como mecanismo de filtro.
- Reavaliar quando o acervo crescer (gatilho sugerido: >300 normas em `normas/`) ou quando
  uma norma revogada deixar de ter efeito residual/analítico.

## Consequences

- Custo: `wiki/normas/` mistura vigentes e revogadas — mitigado pelo campo `status` e pelo
  lint (que permite filtrar).
- Ganho: zero risco de links quebrados (nada muda de caminho), zero mudança no
  `sync_vault_to_build.py` para este caso, e consultas históricas continuam no mesmo lugar.
- Divergência com a mentalidade llm-wiki registrada como decisão consciente, não omissão.
