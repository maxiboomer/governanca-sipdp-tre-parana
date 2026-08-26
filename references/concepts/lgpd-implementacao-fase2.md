---
title: Fase 2 — Implementação do Programa de Compliance LGPD
type: concept
created: 2026-07-27
updated: 2026-07-27
tags: [lgpd, setor-publico, implementacao, ripd, incidentes]
---

# Fase 2 — Implementação do Programa de Compliance

Carregue este arquivo quando o pedido envolver execução do programa (após o diagnóstico): os 16 marcos operacionais, Privacy by Design e by Default, RIPD/DPIA, gerenciamento de incidentes, continuidade de negócios e auditoria interna.

## Os 16 marcos da Fase 2

A Fase 2 estrutura a implementação em 16 marcos operacionais, todos alinhados aos 12 domínios:

1. Gestão de Riscos a Dados Pessoais
2. Política de Segurança de Dados Pessoais
3. Organização da Segurança de Dados Pessoais
4. Gestão de Ativos de Dados Pessoais
5. Segurança de Recursos Humanos
6. Segurança Física e de TI
7. Gestão de Comunicações
8. Controle de Acessos a Dados Pessoais
9. Gestão de Aquisição, Desenvolvimento e Manutenção
10. Gerenciamento de Incidentes
11. Gerenciamento de Continuidade de Negócios
12. Conformidade com a LGPD
13. Treinamento oficial em LGPD
14. Workshop para multiplicadores internos
15. Realização de auditoria interna
16. Elaboração do DPIA / RIPD para tratamentos de alto risco

## Detalhamento estratégico por bloco

### Bloco A — Governança (marcos 1, 2, 3, 12)

**Gestão de Riscos a Dados Pessoais**
- Identificar requisitos de negócio e stakeholders relevantes
- Integrar normas convergentes (ABNT NBR ISO/IEC 27001, 27002, 27701, 22301, COBIT, ITIL)
- Desenvolver roadmap de implementação a partir do relatório de maturidade
- Estabelecer governança permanente (Comitê de Segurança da Informação e Proteção de Dados, com participação do encarregado/DPO)

**Política de Segurança de Dados Pessoais**
- Aprovar e divulgar a POL_01.001 (Política de Segurança da Informação) como guarda-chuva
- Aprovar a POL_05.001 (Política de Proteção de Dados Pessoais) integrada à anterior

**Organização da Segurança**
- Designar formalmente o encarregado (art. 41) por portaria
- Criar o Comitê de Segurança da Informação e Proteção de Dados (composição multidisciplinar: TI, jurídico, RH, áreas finalísticas)
- Definir papéis e responsabilidades (matriz RACI) — insumo para a **MAT_06.002**
- Estabelecer ritos de reunião e prestação de contas

**Conformidade**
- Definir critérios e periodicidade de auditoria interna (PRO_01.001 + PLA_01.001)
- Estabelecer canal de reporte de não conformidades (FRM_10.001)

### Bloco B — Ativos e Privacidade (marcos 4 e 12)

**Gestão de Ativos**
- Construir a MAT_03.001 (Matriz de Ativos da Informação) — ver [lgpd-framework-documental](references/concepts/lgpd-framework-documental.md)
- Aprovar a POL_03.001 (Classificação e Manuseio) e a POL_03.002 (Utilização de Equipamentos)
- Atribuir Asset Owner e Custodian a cada ativo

**Gestão da Privacidade**
- Aprovar a POL_05.001 a POL_05.005 (conjunto de privacidade)
- Implantar o PRO_05.001 (Solicitação de Dados pelo Titular) com prazo e responsável definidos
- Implantar o PRO_05.002 com o FRM_05.001 (LIA, quando aplicável)
- Implantar o PRO_05.003 (Transferência Internacional)
- Implantar o PRO_05.004 (RIPD/DPIA) — detalhe abaixo

### Bloco C — Pessoas (marcos 5, 13, 14)

**Segurança de Recursos Humanos**
- POL_06.001 — política que cobre antes, durante e após a contratação/nomeação
- POL_06.002 — uso aceitável dos ativos
- MAT_06.001 — Matriz de Competências (o que cada cargo precisa saber sobre segurança e privacidade)
- MAT_06.002 — Descrição de Papéis e Atividades
- Termos de confidencialidade no momento da posse e nas mudanças de função

**Treinamento e cultura**
- PLA_06.001 — Plano Anual de Treinamentos
- Treinamento oficial LGPD para o time de privacidade (sugere-se certificação externa)
- Workshop para multiplicadores em cada área
- Material de conscientização contínua: cartazes, intranet, e-mails periódicos, simulações de phishing
- Lista de presença e certificados como evidência de adesão

### Bloco D — Tecnologia (marcos 6, 7, 8, 9)

**Segurança Física e de TI**
- POL_08.001 (Segurança Física)
- POL_08.002 (Proteção Contra Códigos Maliciosos)
- POL_08.003 (Criptografia)
- POL_08.004 (Monitoramento dos Ativos)
- PRO_08.001 (Backup)

**Gestão de Comunicações**
- POL_07.001 (Segurança de Rede)
- POL_07.002 (Acesso à Internet e Mídias Sociais)
- POL_07.003 (Mensagens Eletrônicas)

**Controle de Acessos**
- POL_04.001 (Controle de Acesso) — modelo de concessão (mandatório, discricionário, baseado em papel)
- POL_04.002 (Controle de Acesso Remoto) — VPN, MFA, jump server
- Revisão periódica de acessos como rotina (a cada 6 meses, no mínimo)

**Aquisição, Desenvolvimento e Manutenção**
- POL_09.001 (Desenvolvimento Seguro) — alinhada ao OWASP
- Requisitos de segurança em editais e termos de referência
- Homologação obrigatória pela área de segurança antes do go-live
- Testes de segurança em ambiente de homologação

### Bloco E — Resposta e Continuidade (marcos 10, 11, 15)

**Gerenciamento de Incidentes** — detalhe abaixo
**Continuidade de Negócios** — PLA_11.001 (PCN) — detalhe abaixo
**Auditoria Interna** — detalhe abaixo

### Bloco F — DPIA / RIPD (marco 16) — detalhe abaixo

## Privacy by Design e Privacy by Default

Os marcos da Fase 2 devem incorporar os sete princípios de Privacy by Design (Cavoukian) e a noção de privacidade como padrão:

1. **Proativo, não reativo** — antecipar e prevenir, não corrigir
2. **Privacidade como padrão** — configuração default mais protetiva
3. **Privacidade embarcada no design** — não é "acessório", é parte do sistema
4. **Funcionalidade total** — soma-positiva, não trade-off privacidade × utilidade
5. **Segurança fim-a-fim** — durante todo o ciclo de vida do dado
6. **Visibilidade e transparência** — verificável por todas as partes interessadas
7. **Respeito pela privacidade do usuário** — centralidade do titular

### Critérios práticos para revisão de sistemas

- Confirmar se realmente precisa coletar cada dado (minimização)
- Avaliar uso de pseudonimização e anonimização em ambientes de homologação e estatísticas
- Criptografar dados em repouso e em trânsito
- Gerenciar cookies em portais e implementar política de cookies clara
- Desativar coleta opcional por padrão
- Apagar dados ao revogar consentimento ou cessar a base legal

## RIPD / DPIA — Relatório de Impacto à Proteção de Dados (marco 16)

O **art. 38** da LGPD permite à ANPD determinar a elaboração do relatório. Além disso, é boa prática conduzir um RIPD sempre que:

- O tratamento envolva dados pessoais sensíveis em larga escala
- Houver decisões automatizadas com efeito sobre o titular
- Houver monitoramento sistemático de área pública (câmeras, biometria)
- Houver tratamento de dados de crianças e adolescentes
- Houver tratamento que potencialmente cause discriminação ou exclusão

> **Fonte oficial:** a ANPD mantém página específica com 15 perguntas e respostas sobre o RIPD em `https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/relatorio-de-impacto-a-protecao-de-dados-pessoais-ripd`. O critério oficial para "alto risco", o conteúdo recomendado e a especificidade aplicável ao Poder Público (incluindo determinação de publicação pelo art. 32 da LGPD) estão consolidados em [lgpd-recursos-oficiais-anpd](references/concepts/lgpd-recursos-oficiais-anpd.md). **Consulte essa reference ao redigir o PRO_05.004.**

### Etapas do RIPD (sequência canônica)

1. **Descrição do tratamento** — fluxo completo, finalidade, escopo, atores
2. **Demonstração da necessidade e proporcionalidade** — minimização, base legal
3. **Processo de consulta às partes interessadas** — titulares, áreas, encarregado
4. **Avaliação dos riscos** para os direitos e liberdades dos titulares
5. **Medidas para tratamento dos riscos** — controles técnicos e organizacionais
6. **Documentação** — registro formal do relatório
7. **Monitoramento e revisão** — periodicidade de revalidação

O RIPD é gerenciado pelo **PRO_05.004** e seus achados alimentam a **MAT_05.002 (Matriz de Riscos)**.

### Especificidades para o Poder Público

O **art. 32 da LGPD** confere à ANPD competência para solicitar relatórios de impacto a entidades e órgãos públicos, **incluindo determinação quanto à publicação do RIPD**. Mesmo quando não determinada, a publicação voluntária do RIPD (com versão pública distinta da interna, se houver sigilo legítimo) demonstra aderência aos princípios de livre acesso, transparência e responsabilização do art. 6º. Esta é a posição oficial da ANPD.

## Gerenciamento de Incidentes (marco 10)

### Ciclo conceitual

**Ameaça → Vulnerabilidade → Incidente → Dano**

A gestão de incidentes não começa quando o incidente ocorre, mas no monitoramento contínuo das ameaças e vulnerabilidades. As avaliações que sustentam o programa devem ser:

- **Preventivas** — antes que a ameaça se materialize
- **Repressivas** — durante o incidente, para conter
- **Corretivas** — para restaurar o estado anterior
- **Redutivas** — para reduzir impactos colaterais
- **De recuperação** — para retomar operações normais

### Comunicação de incidente

O **art. 48** obriga a comunicação à ANPD e ao titular quando o incidente puder acarretar **risco ou dano relevante** ao titular. Considerar:

- Não há "se" comunica — é "quando" comunica.
- A **Resolução CD/ANPD nº 15/2024** (Regulamento de Comunicação de Incidente de Segurança) detalha prazos, conteúdo da comunicação e formato. **Esta resolução é a referência operacional vinculante** — releia-a a cada revisão anual do procedimento. Sintetizada em [lgpd-recursos-oficiais-anpd](references/concepts/lgpd-recursos-oficiais-anpd.md).
- A comunicação à ANPD usa o canal oficial CIS: `https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis`
- O **PRO_10.001 (Resposta a Incidentes)** deve operacionalizar prazos e responsáveis alinhados à Res. 15/2024.
- O **PRO_05.001** atende a solicitações de titulares afetados.

### Conteúdo típico da notificação de incidente

- Descrição da natureza do incidente
- Categorias e número aproximado de titulares e registros afetados
- Medidas técnicas e de segurança aplicadas para proteger os dados
- Riscos relacionados ao incidente
- Motivos da demora, se a comunicação não foi imediata
- Medidas adotadas ou propostas para reverter ou mitigar efeitos

## Auditoria Interna (marco 15)

Objetivo: examinar a integridade, adequação e eficácia do programa.

### Sequência operacional

1. Treinamento dos auditores internos
2. Auditoria interna em todo o programa (cobrindo os 12 domínios)
3. Registro das não conformidades no FRM_10.001 e na MAT_10.002
4. Tratamento das não conformidades (ações corretivas e preventivas — PRO.005)
5. Reunião de análise crítica com a alta direção e o Comitê de Segurança da Informação e Proteção de Dados
6. Ajustes no programa

Frequência mínima sugerida: anual, podendo ser maior para domínios críticos. Documentação obrigatória: ata de reunião de análise crítica, planos de ação aprovados e relatório consolidado.

## Continuidade de Negócios (marco 11)

O **PLA_11.001 (Plano de Continuidade de Negócios)** trata da resiliência operacional do órgão diante de eventos disruptivos. Sob a ótica da LGPD, o foco é garantir a **disponibilidade** dos dados pessoais — um dos pilares CIDAL.

Componentes mínimos:

- Análise de impacto no negócio (BIA) com identificação de processos críticos
- Estratégias de recuperação com objetivos definidos (RTO — tempo aceitável de inoperância; RPO — perda máxima aceitável de dados)
- Procedimentos de ativação do plano
- Testes periódicos (tabletop, simulações, testes integrados)
- Atualização do plano após cada teste ou incidente real

Considere a integração com a ABNT NBR ISO 22301 para estruturar o BCMS.

## Marcos de execução prioritários

Quando o órgão tem capacidade limitada para implementar tudo em paralelo, sugere-se a seguinte ordem de prioridade (sem prejuízo do roadmap derivado do relatório de maturidade):

1. Políticas para proteção da privacidade (POL_05.001 a POL_05.005)
2. Designação do encarregado e formação do Comitê
3. Aviso de Privacidade no portal externo (POL_05.002)
4. Procedimento de atendimento ao titular (PRO_05.001) e canal de contato
5. Procedimento de resposta a incidentes (PRO_10.001)
6. Cultura organizacional (PLA_06.001 e treinamento inicial)
7. Adequação de cláusulas contratuais com operadores
8. Matriz de Ativos (MAT_03.001) e Calendário de Retenção (MAT_05.001)
9. RIPD para tratamentos de maior risco (PRO_05.004)
10. Demais documentos do framework
