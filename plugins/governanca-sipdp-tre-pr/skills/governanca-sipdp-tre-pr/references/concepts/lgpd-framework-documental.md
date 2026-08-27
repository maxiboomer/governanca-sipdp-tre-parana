---
title: Framework Documental do Programa LGPD
type: concept
created: 2026-07-27
updated: 2026-07-27
tags: [lgpd, setor-publico, framework-documental, taxonomia]
status: não-aplicável
curadoria: completa
escopo: contextual
---

# Framework Documental do Programa LGPD

Carregue este arquivo quando o pedido envolver: redação ou revisão de qualquer documento do programa, organização da estrutura documental, classificação da informação, matriz de ativos ou taxonomia de códigos.

## Taxonomia padrão

Todos os documentos do programa seguem o código `TIPO_DD.NNN`:

| Tipo | Significado | Característica |
|---|---|---|
| **POL** | Política | Nível estratégico. Declara princípios, diretrizes e responsabilidades. Aprovação no nível mais alto do órgão. Pouco mutável. |
| **PRO** | Procedimento | Nível operacional. Descreve o passo a passo de uma atividade. Mutável conforme processo evolui. |
| **MAT** | Matriz / Inventário | Estrutura de dados (planilha ou base) que registra informações estruturadas (ativos, riscos, papéis, etc.). |
| **FRM** | Formulário | Instrumento para coleta padronizada de informação (LIA, registro de não conformidade, requisição do titular). |
| **PLA** | Plano | Cronograma com metas, ações, responsáveis e prazos (treinamentos, auditorias, continuidade). |

- **DD** = número do domínio (01 a 12)
- **NNN** = sequencial dentro do domínio

## Lista canônica de documentos por domínio

A lista abaixo é o "kit completo" esperado em um programa maduro. Pode ser ajustada ao porte do órgão; o que **não pode** é existir tratamento de dados sem cobertura documental mínima.

### Domínio 1 — Gestão da Segurança / Governança Geral

| Código | Documento |
|---|---|
| POL_01.001 | Política de Segurança da Informação |
| PRO_01.001 | Procedimento de Auditoria Interna |
| PLA_01.001 | Plano Anual de Auditorias |
| MAT_01.001 | Matriz de Controle de Documentos |

Acompanhamento: Manual do Sistema de Gestão da Informação; Ata de Reunião de Análise Crítica.

### Domínio 3 — Gestão de Ativos

| Código | Documento |
|---|---|
| POL_03.001 | Política de Classificação e Manuseio da Informação |
| POL_03.002 | Política de Utilização de Equipamentos |
| MAT_03.001 | Matriz de Ativos da Informação |

### Domínio 4 — Controle de Acesso

| Código | Documento |
|---|---|
| POL_04.001 | Política de Controle de Acesso |
| POL_04.002 | Política de Controle de Acesso Remoto |

### Domínio 5 — Gestão da Privacidade e Proteção de Dados Pessoais

| Código | Documento |
|---|---|
| POL_05.001 | Política de Proteção de Dados Pessoais |
| POL_05.002 | Aviso de Privacidade |
| POL_05.003 | Política Interna de Privacidade |
| POL_05.004 | Política de Contrato com Operadores |
| POL_05.005 | Política de Retenção de Dados |
| PRO_05.001 | Procedimento para Solicitação de Dados Pessoais (atendimento ao titular) |
| PRO_05.002 | Procedimento de Avaliação do Legítimo Interesse |
| FRM_05.001 | Formulário de Avaliação do Legítimo Interesse |
| PRO_05.003 | Procedimento de Transferência Internacional de Dados Pessoais |
| PRO_05.004 | Procedimento para RIPD / DPIA |
| MAT_05.001 | Calendário de Retenção de Dados |
| MAT_05.002 | Matriz de Riscos do RIPD |

### Domínio 6 — Segurança de Recursos Humanos

| Código | Documento |
|---|---|
| POL_06.001 | Política de Segurança de Recursos Humanos |
| POL_06.002 | Política de Controle de Uso Aceitável dos Ativos |
| PLA_06.001 | Plano Anual de Treinamentos |
| MAT_06.001 | Matriz de Competências |
| MAT_06.002 | Matriz de Descrição de Papéis e Atividades |

Acompanhamento: Termo de Uso de Sistemas de Informação; Termo de Confidencialidade.

### Domínio 7 — Gestão de Comunicações

| Código | Documento |
|---|---|
| POL_07.001 | Política de Segurança de Rede |
| POL_07.002 | Política de Acesso a Internet e Mídias Sociais |
| POL_07.003 | Política de Mensagens Eletrônicas |

### Domínio 8 — Segurança Física e de TI

| Código | Documento |
|---|---|
| POL_08.001 | Política de Segurança Física |
| POL_08.002 | Política de Proteção Contra Códigos Maliciosos |
| POL_08.003 | Política de Criptografia |
| POL_08.004 | Política de Monitoramento dos Ativos de Informação |
| PRO_08.001 | Procedimento de Backup |

### Domínio 9 — Aquisição, Desenvolvimento e Manutenção de Sistemas

| Código | Documento |
|---|---|
| POL_09.001 | Política de Desenvolvimento Seguro |

### Domínio 10 — Gerenciamento de Incidentes

| Código | Documento |
|---|---|
| POL_10.001 | Política de Resposta a Incidentes de Segurança da Informação |
| PRO_10.001 | Procedimento de Resposta a Incidentes |
| PRO_10.002 | Procedimento de Registro de Não Conformidades |
| FRM_10.001 | Formulário de Registro de Não Conformidades |
| MAT_10.001 | Matriz de Riscos (operacionais) |
| MAT_10.002 | Matriz de Não Conformidades |

### Domínio 11 — Continuidade de Negócios

| Código | Documento |
|---|---|
| PLA_11.001 | Plano de Continuidade de Negócios |

## Conteúdo mínimo dos documentos principais

### POL_03.001 — Política de Classificação e Manuseio da Informação

**Objetivo:** estabelecer critérios para identificar, classificar e tratar todos os ativos de informação, mitigando risco de vazamento, acessos indevidos e modificações não autorizadas.

**Níveis de classificação (obrigatórios):**

1. **Pública** — acesso livre. Ex.: editais publicados, decisões públicas, atos normativos divulgados no portal.
2. **Interna** — circulação restrita ao corpo funcional. Não causa dano catastrófico se vazada, mas não deve ser exposta externamente sem critério. Ex.: comunicados internos, manuais administrativos, listas de ramais.
3. **Confidencial** — dados sensíveis, informações estratégicas ou dados pessoais protegidos por lei. Acesso restrito por necessidade de serviço. Ex.: folhas de pagamento detalhadas, avaliações de desempenho, termos contratuais em análise.
4. **Secreta** — segurança institucional máxima ou processos sob sigilo estrito. Vazamento compromete o Estado, a instituição ou investigações. Ex.: credenciais de infraestrutura crítica, chaves criptográficas, auditorias internas sigilosas, dados sob sigilo judicial estrito.

**Diretrizes mínimas de manuseio:**

- **Rotulagem:** documento Confidencial ou Secreto deve trazer marcação visível no cabeçalho ou rodapé.
- **Armazenamento físico:** arquivos confidenciais em armários trancados com controle de chaves; arquivos digitais em pastas de rede com permissões restritas via diretório corporativo (LDAP/AD).
- **Descarte:** documentos impressos confidenciais ou secretos não vão para o lixo comum; passam por fragmentadora que impossibilite reconstrução do texto. Mídias digitais (HDs, fitas, pen-drives) sofrem desmagnetização ou destruição física.

**Atenção LAI vs. LGPD:** documentos públicos sob a LAI podem conter dados pessoais que precisam ser anonimizados antes da divulgação. A política deve descrever esse fluxo de compatibilização.

### POL_03.002 — Política de Utilização de Equipamentos

**Responsabilidades do usuário:**

- **Uso exclusivo:** equipamentos institucionais (desktops, notebooks, tablets, smartphones funcionais) são para uso estritamente profissional.
- **Guarda e zelo:** o colaborador responde civil e administrativamente pela integridade do ativo sob sua custódia.
- **Bloqueio de tela:** obrigatório o bloqueio imediato ao se ausentar do posto, independentemente do tempo.

**Proibições mínimas:**

- Instalação de softwares, extensões ou aplicativos sem homologação da área de TI.
- Uso de mídias removíveis pessoais (pen-drives, HDs externos) para cópia ou extração de dados institucionais.
- Conexão a redes externas em modo home office sem VPN oficial e MFA ativado.

### MAT_03.001 — Matriz de Ativos da Informação

Inventário centralizado de todos os ativos de informação. Cada item deve preencher obrigatoriamente:

| Campo | Conteúdo |
|---|---|
| ID do Ativo | Código único (A001, A002, ...) |
| Nome do Ativo | Sistema, banco de dados ou conjunto documental (ex.: Sistema de Gestão de RH, Prontuários Físicos) |
| Descrição Operacional | Funções e dados que o ativo processa |
| Proprietário (Asset Owner) | Unidade administrativa ou gestor responsável pelo ciclo de vida do ativo |
| Custodiante (Asset Custodian) | Equipe técnica (geralmente TI) responsável por infraestrutura, backup e segurança |
| Classificação | Nível conforme POL_03.001 (Pública, Interna, Confidencial, Secreta) |
| C — Confidencialidade | Nota Alto/Médio/Baixo |
| I — Integridade | Nota Alto/Médio/Baixo |
| D — Disponibilidade | Nota Alto/Médio/Baixo |
| Base legal aplicável | Inciso do art. 7º ou art. 11 da LGPD |
| Categorias de dados pessoais tratados | Gerais, sensíveis, de crianças |
| Período de retenção | Conforme POL_05.005 e MAT_05.001 |
| Compartilhamentos | Internos e externos |

A matriz alimenta o RIPD, a análise de riscos e o plano de continuidade. Mantenha-a viva — não trate como documento "feito uma vez e arquivado".

### POL_05.001 — Política de Proteção de Dados Pessoais

Estrutura sugerida:

1. **Objetivo e escopo**
2. **Definições** — alinhadas ao art. 5º da LGPD
3. **Princípios aplicáveis** — os 10 princípios do art. 6º
4. **Bases legais utilizadas pelo órgão** — citar quais incisos do art. 7º e art. 11 são aplicáveis
5. **Direitos do titular e canal de atendimento** — referência ao PRO_05.001
6. **Encarregado (DPO)** — designação, atribuições, forma de contato
7. **Responsabilidades** — alta direção, áreas finalísticas, TI, encarregado
8. **Sanções aplicáveis** — internas (disciplinares) e externas (ANPD, civis)
9. **Articulação com a LAI e demais normas correlatas**
10. **Revisão e vigência**

### POL_05.002 — Aviso de Privacidade

Documento **externo**, para titulares e cidadãos. Linguagem clara, sem juridiquês. Deve responder pelo menos:

- Quem somos (controlador)
- Quais dados coletamos
- Para que coletamos (finalidade)
- Sob qual base legal (citar art. 7º e/ou 11)
- Com quem compartilhamos
- Por quanto tempo guardamos
- Quais são seus direitos e como exercê-los
- Como nos contatar (encarregado/DPO)

Publicar no portal institucional em local de fácil acesso (rodapé é prática comum).

### POL_05.003 — Política Interna de Privacidade

Voltada ao público **interno**. Estabelece regras práticas para o dia a dia: o que servidor pode/não pode fazer com dados de cidadãos, regras para envio por e-mail, uso de impressoras, descarte, conduta em home office, uso de IA generativa com dados institucionais.

### POL_05.004 — Política de Contrato com Operadores

Define os requisitos mínimos a serem exigidos em contratos com terceiros que tratem dados em nome do controlador. Inclui:

- Cláusulas LGPD obrigatórias (ver Etapa 3 da Fase 1)
- Padrões mínimos de segurança a serem comprovados (certificações, auditoria)
- Procedimento para autorização de subcontratação
- Direito de auditoria
- Tratamento de incidentes e prazos de notificação
- Disposições para encerramento contratual (devolução ou eliminação dos dados)

### POL_05.005 — Política de Retenção de Dados

Define os prazos de guarda e os critérios para descarte seguro. Alinhar com:

- Legislação específica (ex.: tabelas de temporalidade documental, prazos prescricionais aplicáveis)
- Necessidade operacional
- Direito do titular à eliminação

Operacionalizada pelo **MAT_05.001 (Calendário de Retenção)**.

### PRO_05.001 — Procedimento para Solicitação de Dados Pessoais

Fluxo completo do atendimento a requisições do titular (art. 18):

1. Recebimento — canal único (e-mail do encarregado, formulário online)
2. Triagem — autenticação do titular, identificação do tipo de pedido
3. Análise técnica — área detentora dos dados
4. Análise jurídica — viabilidade legal da solicitação
5. Resposta — formal, dentro do prazo
6. Registro — para fins de accountability e auditoria

Prazo legal: 15 dias para confirmação e acesso (art. 19, §1º); pedidos de correção, eliminação e demais providências têm prazo razoável.

### PRO_05.002 + FRM_05.001 — Avaliação de Legítimo Interesse (LIA)

Aplicável quando se usa legítimo interesse como base legal. Estrutura mínima do FRM:

1. **Teste de propósito** — qual o interesse legítimo perseguido?
2. **Teste de necessidade** — o tratamento é necessário para o propósito? Há alternativas menos invasivas?
3. **Teste de balanceamento** — o interesse prevalece sobre os direitos do titular? Expectativa razoável do titular?
4. **Salvaguardas adotadas** — minimização, anonimização, criptografia, opt-out
5. **Conclusão e responsável pela aprovação**

LIA não vale para dados sensíveis.

### MAT_06.002 — Matriz de Descrição de Papéis e Atividades

Atrelada à governança de acessos. Para cada cargo/lotação, mapeia o que a pessoa pode fazer e em quais sistemas, evitando acúmulo excessivo de privilégios (princípio do menor privilégio). Insumo direto para a configuração de perfis no controle de acesso.

## Princípios para redigir cada documento

1. **Comece pelo objetivo.** Uma frase clara que diga para que serve.
2. **Defina o escopo.** A quem e a quê o documento se aplica.
3. **Use verbo imperativo.** "Deve", "é vedado", "fica obrigado" — nunca "recomenda-se", "seria bom".
4. **Atribua responsáveis nominais (por cargo, não por pessoa).** Quem aprova, quem executa, quem fiscaliza.
5. **Cite a base legal.** Artigos da LGPD que fundamentam cada controle.
6. **Inclua sanções por descumprimento.** Disciplinares internas, sem prejuízo das demais cabíveis.
7. **Defina vigência e periodicidade de revisão.** Toda política deve ser revisada — sugere-se anualmente ou em caso de evento relevante (incidente, mudança normativa).
8. **Mantenha controle de versões.** Histórico de revisões registrado.

## Cuidado com a tentação do "copy-paste"

Modelos prontos servem como referência, mas o que vale é o ajuste à realidade do órgão. Uma política copiada de outro órgão e implementada sem adaptação **gera mais risco que segurança** — porque a alta direção assina um documento que não reflete os processos reais, e essa lacuna aparece na primeira auditoria ou no primeiro incidente.
