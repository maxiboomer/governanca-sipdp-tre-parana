---
status: accepted
date: 2026-08-26
---

# Acervo amplo de normas do TRE-PR, com camada curada de SI/PDP

O nome do plugin promete SI/PDP, mas dos 154 textos reunidos apenas ~23 têm tema de SI/PDP
evidente e 10 não têm relação nenhuma (calendário de feriados, plantão judiciário, prestação
pecuniária, teletrabalho). Em vez de podar o acervo para o nome caber, assumimos o escopo
real: o acervo é de **normas internas do TRE-PR e da JE**, e SI/PDP é a **camada de
curadoria** por cima dele.

## Considered Options

- **Podar** o acervo para só SI/PDP/continuidade. Rejeitado: descarta coleta já feita e não
  resolve o problema real, que é a descrição prometer menos do que a base carrega — o que
  faz o Claude não consultá-la quando deveria.
- **Deixar a incoerência.** Rejeitado: a descrição é o que determina quando a skill ativa.

## Consequences

A colisão com a skill `monitoramento-normas-secti` deixa de ser sobreposição parcial e passa
a ser duplicação frontal — as duas passam a declarar o mesmo universo. A consolidação entre
elas vira questão de quando, não de se. Decisão ainda em aberto.
