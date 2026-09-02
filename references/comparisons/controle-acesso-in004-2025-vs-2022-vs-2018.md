---
title: "Comparação Controle de Acesso — IN 004/2025 × IN 004/2022 × IN-DG 2018"
name: "Comparação Controle de Acesso — IN 004/2025 × IN 004/2022 × IN-DG 2018"
created: 2026-09-02
updated: 2026-09-02
type: comparison
confidence: high
contested: false
status: não-aplicável
curadoria: completa
escopo: contextual
tags: [controle-acesso, seguranca-informacao, comparacao, tre-pr, identidade]
sources: [raw/tre-pr-in-instrucao-normativa-004-de-28-de-maio-de-2025.md, raw/tre-pr-in-instrucao-normativa-004-de-08-de-novembro-de-2022.md]
---

# Comparação Controle de Acesso — IN 004/2025 × IN 004/2022 × IN-DG 2018

## O que está sendo comparado e por quê

O controle de acesso lógico/físico no TRE-PR evoluiu em três gerações. Compreender a cadeia é
essencial para responder "o que vale hoje" e "o que foi consolidado": as IN-DG de 2018
(contas/senhas, internet, serviços) foram **revogadas pela IN 004/2022** (art. 28), que por sua
vez é a norma geral de uso de recursos computacionais. A **IN 004/2025** (gestão de identidade e
controle de acesso) é a norma específica atual — **complementar** à 004/2022, sem revogá-la.

## Dimensões de comparação

| Dimensão | IN-DG 08/2018, 09/2018, 12/2018 (REVOGADAS) | IN 004/2022 (vigente — uso de recursos) | IN 004/2025 (vigente — identidade e acesso) |
|---|---|---|---|
| **Situação** | Revogadas pela IN 004/2022, art. 28 | Vigente | Vigente (complementar) |
| **Objeto** | Contas/senhas; acesso à internet; acesso a serviços | Uso geral dos recursos computacionais | Gestão de identidade + controle de acesso lógico e físico |
| **Princípios** | — | — | Necessidade de saber, necessidade de uso, privilégio mínimo, segregação de funções (art. 4º) |
| **Identidade** | — | — | Identificação única (art. 23); criação automática via fontes autoritativas (art. 21); inventário de contas com revisão trimestral (art. 18) |
| **Senhas** | Regras básicas | Regras gerais | Política completa: 8/14+ caracteres, MFA obrigatório p/ acesso remoto/administrativo, troca em ≤3 meses, hash com salt, bloqueio após 5 tentativas (arts. 34-41) |
| **Acesso privilegiado** | — | — | Credenciais exclusivas, prazo de expiração, avaliação mensal, ferramenta PAM (arts. 29-32) |
| **Acesso físico** | — | — | Perímetro do datacenter, videomonitoramento, portas corta-fogo, detecção de intrusos (arts. 7-11) |
| **Código-fonte** | — | — | Acesso restrito, ferramentas segregadas, registro de eventos (art. 51) |
| **Rede/VPN** | Acesso à internet e serviços | Regras gerais | Regras específicas: bloqueio de equipamentos pessoais, registro 3 meses, MFA opcional na VPN (arts. 42-50) |

## Veredito / síntese

- **A IN 004/2025 é a norma técnica atual de controle de acesso** — muito mais completa que as
  IN-DG 2018 que a precederam (que tratavam só de senhas/internet).
- **A IN 004/2022 permanece vigente como norma geral de uso de recursos**; a 004/2025 é a camada
  especializada (identidade, acesso físico/lógico, privilégio). Não há revogação entre elas —
  trabalhar as duas juntas: 004/2022 para uso aceitável, 004/2025 para quem acessa o quê.
- **Referências a IN-DG 2018** em documentos antigos devem ser atualizadas para a IN 004/2025
  (controle de acesso) ou IN 004/2022 (uso de recursos).

## Fontes

^[raw/tre-pr-in-instrucao-normativa-004-de-28-de-maio-de-2025.md]
^[raw/tre-pr-in-instrucao-normativa-004-de-08-de-novembro-de-2022.md]

## Relações

- [[wiki/normas/tre-pr-in-instrucao-normativa-004-de-28-de-maio-de-2025]]
- [[wiki/normas/tre-pr-in-instrucao-normativa-004-de-08-de-novembro-de-2022]]
- [[wiki/normas/tre-pr-in-dg-08-2018-contas-senhas]]
- [[wiki/normas/tre-pr-in-dg-09-2018-acesso-internet]]
- [[wiki/concepts/governanca-ti]]
- [[wiki/concepts/seguranca-informacao-justica-eleitoral]]
