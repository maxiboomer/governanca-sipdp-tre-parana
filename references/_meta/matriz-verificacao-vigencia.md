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

## Critério

A matriz separa confirmação por fonte oficial, revogação expressa no texto e situação ainda pendente. Localizar uma página oficial confirma a existência/publicação do ato, mas não necessariamente prova que não houve alteração posterior.

## Resultado consolidado

Todas as **168 páginas de normas** tiveram seu status verificado nesta rodada:

| Status | Qtd | Critério |
|---|---|---|
| **Vigente** | 135 | Publicação localizada no compilado oficial (TRE-PR/TSE/CNJ) ou em lei vigente |
| **Revogada** | 18 | Revogação expressa no próprio texto ou em norma posterior |
| **Outros** | 15 | Históricas / de composição / não-aplicáveis |

Não restam normas com `status: não-confirmada`.

## Base de verificação

A verificação foi feita cruzando as páginas do vault com:

1. **Compilado oficial do TRE-PR** — listagens de Instruções Normativas, Resoluções, Normas
   Técnicas da SECTI, Portarias da Presidência/Diretoria-Geral e Portarias Conjuntas, por ano.
2. **Compilado oficial do TSE** — resoluções e portarias localizadas por busca no portal.
3. **Atos do CNJ** — cadastro oficial (atos.cnj.jus.br).
4. **Texto integral em `raw/`** — para revogações expressas no próprio ato.

## Notas de confiabilidade

- **Compilado oficial é suficiente para "trabalhar", mas a citação em documento exige DJE/DOU.**
  Para uso formal, subir a referência ao DJE (ver ADR 0002).
- Algumas normas antigas (ex.: Res. 735/2016, 756/2017, OS 04/2009) permanecem no compilado e
  foram mantidas como `vigente`, mas é prudente reavaliar se ainda têm aplicação prática.
- **Portarias de composição de comitês e equipes** foram classificadas como vigentes pela presença
  no portal, mas são substituídas por atos posteriores de nomeação; verificar a composição atual
  antes de usar.
- **Res. TSE 23.650/2021 (PGPPDP)** tinha duplicidade com denominação incorreta
  (`pgppdp-tse-23650-2021.md`, chamada de "Plano Geracional de Proteção e Defesa"). A página
  canônica é `tse-resolucao-23-650-2021-pgppdp.md`; a duplicidade virou alias com nota de correção.

## Alertas de conteúdo

- A Resolução TSE 23.763/2026 é a referência atual de PSI nacional; as Resoluções 23.501/2016 e
  23.644/2021 são `revogadas` (históricas).
- A IN 010/2025 revoga expressamente a IN 006/2018.
- As INs 001/2018, 008/2018, 009/2018 e 012/2018 foram revogadas pela IN 004/2022 (art. 28).
- A revisão periódica deve considerar alterações, revogações parciais e atos posteriores.
