---
title: "Matriz de verificação de vigência normativa"
created: 2026-08-26
updated: 2026-08-26
type: metadata
status: não-aplicável
curadoria: completa
escopo: contextual
tags: [metadados, vigencia, auditoria]
---

# Matriz de verificação de vigência normativa

## Resultado consolidado (reavaliação completa — 2026-08-26)

Todas as **168 páginas de normas** têm status definitivo:

| Status | Qtd | Critério |
|---|---|---|
| **Vigente** | 136 | Publicação localizada no compilado oficial (TRE-PR/TSE/CNJ) ou lei vigente |
| **Revogada** | 19 | Revogação expressa no próprio texto ou em norma posterior |
| **Histórica** | 12 | Plano de período encerrado / instrumento superado por versão mais recente |
| **Não-aplicável** | 1 | Sem status jurídico aplicável |
| **Sem status** | 0 | — |

## Erros corrigidos nesta reavaliação

1. **10 normas de SI/PDP ficaram sem status** por grafia variante do campo (`Não confirmado`
   em vez de `não-confirmada`), que meus scripts de atualização não capturaram. Eram normas
   centrais: IN 07/2018 (backup), IN 08/2019 (vulnerabilidades), OS 07/2017 (criptografia),
   Portaria 247/2021 (DPO), Portaria DG 086/2026 (CGSI/PDP), Res. 959/2025 (IA), Res. 962/2025
   (Comitê de crises) e NTs SECTI 02/2022, 05/2020 e 08/2020. **Todas foram reavaliadas e
   classificadas** (majoritariamente vigentes, exceto a OS 07/2017, marcada como histórica por
   ter sido regulada de forma atual pela IN 003/2025 sobre criptografia).

2. **OS 08/2017 (MDS)** estava marcada como `vigente`, mas é **revogada** — a Portaria TRE-PR DG
   132/2026 a revoga expressamente ("Revogar a Ordem de Serviço nº 08, de 18/12/2017").

3. **Planos de período encerrado** marcados como `histórica`:
   - Res. 735/2016 (PETI 2016-2020)
   - Portaria 350/2021 (PDTI 2021-2022)
   - Portaria 341/2023 (PDTI 2023-2024)
   - Portaria 133/2023 (PAC 2023)
   - Res. 874/2021 (revisão do PEI 2021-2026)

4. **NTs superadas por versões mais recentes** marcadas como `histórica`:
   - NT 003/2022 (planejamento orçamentário) → NT 004/2026
   - NT 003/2024 (plano de gestão de riscos) → NT 001/2025

## O que permanece como decisão de curadoria (não automatizável)

- **Portarias de composição/designação** de comitês, comissões e equipes (ex.: comitê de gestão
  de TI, equipes de trabalho, designações de membros) foram mantidas como vigentes quando
  presentes no portal, mas são **substituídas por atos posteriores de nomeação**. Verificar a
  composição atual antes de usar.
- **Normas antigas mantidas no compilado** (Res. 756/2017 e 779/2017 de governança, Res. 815/2018
  de contratações, OS 04/2009 de equipamentos) permanecem formalmente vigentes, pois são citadas
  como base legal em normas atuais (ex.: a Res. 932/2024 referencia a 756/2017). É prudente
  reavaliar a aplicação prática, mas **não há revogação expressa localizada**.
- A distinção `vigente` × `histórica` para planos temporais depende de confirmar se o período do
  plano já expirou.

## Confiabilidade

- **Compilado oficial é suficiente para "trabalhar"**, mas a citação em documento exige DJE/DOU
  (ver ADR 0002).
- Normas marcadas `revogada` têm a revogação **expressa** em norma posterior identificada
  (IN 010/2025 → IN 006/2018; IN 004/2022 → INs 001, 008, 009, 012/2018; Portaria 132/2026 →
  OS 08/2017; Res. TSE 23.763/2026 → 23.644/2021 → 23.501/2016).
