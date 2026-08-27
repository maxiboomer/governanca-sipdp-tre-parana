---
title: Fase 1 — Diagnóstico (Gap Analysis LGPD)
type: concept
created: 2026-07-27
updated: 2026-07-27
tags: [lgpd, setor-publico, diagnostico, gap-analysis]
status: não-aplicável
curadoria: completa
escopo: contextual
---

# Fase 1 — Diagnóstico (Gap Analysis LGPD)

Carregue este arquivo quando o pedido envolver levantamento da situação atual, mapeamento de bases de dados pessoais, ciclo de vida dos dados, ou produção do relatório de maturidade inicial.

## Objetivo da Fase 1

Levantar a situação atual do órgão em relação à LGPD, mapeando onde estão os dados pessoais, como são tratados, sob qual base legal, com quais riscos e em qual nível de maturidade. O produto final é um **relatório de maturidade** que serve de linha de base para o planejamento da Fase 2.

## Visão geral das 8 etapas

| # | Etapa | Produto |
|---|---|---|
| 1 | Mapeamento das áreas e dos tratamentos | Inventário de tratamentos por área |
| 2 | Desenho do ciclo de vida dos dados pessoais | Diagramas de processo (coleta → eliminação) |
| 3 | Análise de contratos e termos | Levantamento de cláusulas faltantes; matriz de fornecedores/operadores |
| 4 | Análise de políticas e procedimentos | Lista de lacunas documentais (gap documental) |
| 5 | Análise da infraestrutura física e de TI | Relatório de pentest e avaliação de configurações |
| 6 | Identificação das bases de dados pessoais | Catálogo de bases por categoria e base legal |
| 7 | Avaliação de maturidade nos 12 domínios | Notas 0–5 por domínio |
| 8 | Relatório de maturidade | Documento consolidado; insumo para a Fase 2 |

## Etapa 1 — Mapeamento das áreas e dos tratamentos

Cada unidade administrativa preenche um questionário identificando seus tratamentos. O resultado é um inventário que alimenta as etapas seguintes.

### Checklist para o controlador (a ser respondido por cada área)

1. O seu departamento coleta ou processa dados pessoais?
2. Quais dados pessoais são mais comumente coletados?
3. De quem são os dados pessoais coletados? (servidores, cidadãos, fornecedores, terceiros)
4. Qual a finalidade ou resultado do processamento?
5. São tratados dados pessoais de menores de idade ou de pessoas incapacitadas?
6. O departamento obtém algum ganho ou benefício específico com o processamento?
7. O departamento processa dados como resultado de contrato?
8. O departamento tem total autonomia sobre como os dados são processados? (ajuda a definir se é controlador ou operador)
9. São designados operadores (terceiros) para processar os dados?

Cada resposta "sim" abre uma frente de aprofundamento na Etapa 2 (ciclo de vida) e na Etapa 6 (catálogo de bases).

## Etapa 2 — Desenho do ciclo de vida dos dados pessoais

Para cada tratamento identificado na Etapa 1, desenhar o fluxo completo: coleta → processamento → análise → compartilhamento → armazenamento → reutilização → eliminação.

### Pontos de coleta típicos no setor público

- Atendimento presencial
- Formulários físicos
- E-mail institucional
- Portal web (cadastros, peticionamento eletrônico)
- Sistemas internos integrados
- APIs entre órgãos
- Telefone

### Pontos críticos a documentar para cada fluxo

- Quem coleta (papel/cargo) e onde armazena (sistema/repositório)
- Base legal aplicável (cumprimento de obrigação, políticas públicas, execução de contrato etc.)
- Compartilhamentos internos (entre áreas) e externos (outros órgãos, fornecedores)
- Prazo de retenção previsto (alinhado à futura POL_05.005)
- Forma de eliminação prevista

O produto desta etapa é a base direta para a futura **MAT_03.001 (Matriz de Ativos)** e para o **MAT_05.001 (Calendário de Retenção)**.

## Etapa 3 — Análise de contratos e termos

Levantar e revisar todos os instrumentos que envolvam tratamento de dados. Três focos principais:

- **Colaboradores** (servidores, estagiários, terceirizados) — termos de confidencialidade, termo de uso de sistemas, regras de conduta. Insumo para a futura **POL_06.001** e o **Termo de Uso de Sistemas de Informação**.
- **Cidadãos / titulares de serviços** — termos de adesão, avisos de privacidade em portais, formulários de coleta. Insumo para o **POL_05.002 (Aviso de Privacidade)**.
- **Fornecedores e operadores** — contratos administrativos, atas de registro de preços, convênios, termos de cooperação. Avaliar a presença de cláusulas LGPD obrigatórias. Insumo para **POL_05.004 (Política de Contrato com Operadores)** e para aditivos contratuais.

### Cláusulas mínimas a verificar em contratos vigentes

- Finalidade e bases legais expressas
- Obrigação do operador de tratar dados apenas conforme instruções do controlador
- Medidas de segurança técnicas e administrativas exigidas
- Obrigação de notificação imediata de incidentes
- Direito de auditoria pelo controlador
- Subcontratação só com autorização prévia
- Devolução ou eliminação dos dados ao término do contrato
- Responsabilidade solidária quando aplicável (art. 42, §1º)

A ausência ou insuficiência dessas cláusulas em contratos vigentes vira **lista de aditivos a celebrar**.

## Etapa 4 — Análise de políticas e procedimentos

Diagnosticar a estrutura documental existente em três camadas hierárquicas:

1. **Política** — nível estratégico; declara princípios e diretrizes.
2. **Diretriz / Norma** — nível tático; estabelece regras gerais para um tema.
3. **Procedimento** — nível operacional; descreve o passo a passo.

O resultado é um **gap documental** comparando o existente com a lista esperada pelo framework (ver [[concepts/lgpd-framework-documental]]).

## Etapa 5 — Análise da infraestrutura física e de TI

Avaliação em duas vertentes principais.

### Vertente física

- Áreas de trabalho (acesso restrito, mesa limpa, mesa-livre)
- Equipamentos (estações, multifuncionais, equipamentos de rede)
- Armazenamento de documentos físicos (armários, arquivos, sala-cofre)
- Descarte (fragmentadora, desmagnetização de mídias)
- Câmeras de monitoramento (incluindo análise da própria base de imagens como dado pessoal)

### Vertente lógica

- Arquitetura de rede (segmentação, DMZ, perímetro)
- Equipamentos (firewalls, IDS/IPS, proxies, servidores)
- Configurações (hardening, baselines, atualização de patches)
- Soluções implementadas (antivírus, SIEM, DLP, backup, criptografia)
- Mídias de armazenamento (controle de uso de mídias removíveis)

### Testes de invasão e varredura

- **Scan de vulnerabilidades** — varredura automatizada periódica
- **Pentest Black Box** — testador sem conhecimento prévio da infraestrutura
- **Pentest White Box** — testador com acesso a documentação e código
- **Pentest Gray Box** — modelo híbrido

Os resultados alimentam o domínio 8 (Segurança Física e de TI) e o domínio 10 (Incidentes).

## Etapa 6 — Identificação das bases de dados pessoais

Catálogo consolidado de todas as bases tratadas pelo órgão. Para o setor público, sugere-se a seguinte categorização inicial (a ser ajustada à realidade do órgão):

| Base | Categorias de titulares (exemplos) | Bases legais típicas |
|---|---|---|
| 1 | Cidadãos / usuários de serviços | Cumprimento de obrigação legal; execução de políticas públicas |
| 2 | Servidores e ex-servidores | Cumprimento de obrigação legal (legislação trabalhista/estatutária) |
| 3 | Candidatos (concursos, processos seletivos) | Execução de políticas públicas; cumprimento de obrigação legal |
| 4 | Estagiários e terceirizados | Execução de contrato; cumprimento de obrigação legal |
| 5 | Fornecedores (pessoas físicas e representantes de PJ) | Execução de contrato; cumprimento de obrigação legal |
| 6 | Visitantes | Legítimo interesse (avaliar via LIA) |
| 7 | Outras bases específicas do órgão | Variável |

### Operadores típicos a mapear

- Empresas contratadas para serviços de TI e processamento
- Empresas de gestão de benefícios (vale-alimentação, plano de saúde)
- Contabilidade ou folha terceirizada
- Empresas de manutenção predial com acesso a áreas restritas
- Bancos pagadores
- Empresas de pesquisa quando o órgão patrocina estudos

Cada operador identificado precisa estar coberto por contrato com cláusulas LGPD adequadas (ver Etapa 3).

## Etapas 7 e 8 — Avaliação e relatório de maturidade

A avaliação utiliza a escala de maturidade 0–5 aplicada aos 12 domínios, considerando cinco áreas de foco transversais (Visão, Processos, Pessoas, Tecnologia, Cultura). O detalhamento da metodologia de avaliação está em [[concepts/lgpd-maturidade-avaliacao]].

### Estrutura sugerida do Relatório de Maturidade

1. Sumário executivo (1–2 páginas, com nota global)
2. Metodologia adotada
3. Escopo (áreas, sistemas e processos avaliados)
4. Resultados por domínio (12 seções, com nota e justificativa)
5. Riscos críticos identificados
6. Matriz de prioridades (urgência × impacto)
7. Recomendações para a Fase 2 (roadmap inicial)
8. Anexos (questionários, evidências, fluxos desenhados)

O relatório de maturidade **é a fronteira entre Fase 1 e Fase 2**. Sem ele, a Fase 2 vira ação sem direção.
