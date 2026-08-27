---
title: PSI do Paraná — Res. TRE-PR 974/2026
type: norma
created: 2026-07-27
updated: 2026-07-27
tags: [psi, seguranca-informacao, tre-pr]
status: vigente
curadoria: completa
escopo: contextual
sources: [raw/psi-tre-pr-974-2026.md]
status_verificacao: "Verificado em 2026-08-26; consultar DJE/DOU para citação formal."
---

# PSI do Paraná — Res. TRE-PR 974, de 15/4/2026

Política de Segurança da Informação no âmbito da Justiça Eleitoral do Paraná.
**[Verificado contra o texto oficial compilado do TRE-PR em 22/7/2026 — 18 artigos, 6 capítulos.
Todas as transcrições deste arquivo conferem com o original.]**
Publicada no DJE-TRE-PR nº 070, de 20/4/2026. Entrou em vigor na data da publicação
(art. 18). Prevê **revisão anual** ou sempre que houver alteração significativa no
ambiente tecnológico ou no arcabouço normativo nacional (art. 17).

> **Alerta de descompasso normativo (essencial):** a 974/2026 foi editada em 15/4/2026 e,
> em seus considerandos, ancora-se na **Res. TSE 23.644/2021 — que foi revogada** pela
> Res. TSE 23.763/2026 (de 9/6/2026, posterior à 974). Portanto, a PSI local regulamenta
> a PSI nacional **antiga**. Até a revisão de alinhamento (prazo da norma nacional:
> 31/12/2027), trabalhe com as duas normas lado a lado e sinalize divergências. Onde
> houver conflito, prevalece a norma nacional (TSE > TRE).

---

## Estrutura da Resolução

- Cap. I — Disposições preliminares e escopo (art. 1º-4º)
- Cap. II — Deveres e uso aceitável dos recursos (art. 5º-6º)
- Cap. III — Estrutura de governança de SI (art. 7º-9º)
- Cap. IV — Tratamento da informação e controles de acesso (art. 10-12)
- Cap. V — Continuidade de negócios (art. 13)
- Cap. VI — Disposições finais e penalidades (art. 14-18)

---

## Princípios (art. 2º)

Disponibilidade, integridade, confidencialidade, autenticidade, **irretratabilidade**
e **auditabilidade**.

> Este rol corresponde ao antigo "DICA+AI" da revogada 23.644/2021. **Diverge** da PSI
> nacional vigente (23.763/2026, art. 3º), que adota disponibilidade, integridade,
> confidencialidade, autenticidade e **não repúdio** (sem irretratabilidade nem
> auditabilidade como princípios).
>
> **Mas a divergência é menor do que parece — e a 974 se contradiz.**
>
> 1. **Irretratabilidade:** a 974 não a define. A definição aplicável é a da Portaria
>    TSE 444/2021, art. 2º, XXXIV, que equipara **"irretratabilidade (ou não repúdio)"**
>    como sinônimos. Logo, quanto a esse princípio a divergência é **nominal**.
> 2. **Auditabilidade é a única divergência real** — e é frágil dentro da própria 974:
>    - não é definida no art. 4º (que traz 34 definições);
>    - não consta da Portaria TSE 444/2021;
>    - **o art. 4º, XXX da própria 974 define "segurança da informação" como orientada
>      por autenticidade, confidencialidade, integridade, disponibilidade e
>      irretratabilidade — SEM auditabilidade.**
>
> **Incoerência interna:** o art. 2º eleva a auditabilidade a princípio norteador; o
> art. 4º, XXX a exclui do conceito de segurança da informação. Consequência prática:
> se a revisão de alinhamento retirar a auditabilidade do art. 2º, **não há perda
> normativa real** — o próprio texto local já não a incorpora ao seu conceito central.
> Argumento útil para desarmar resistência à revisão.

---

## Destinatários (art. 3º)

Magistrados, membros do MP, servidores efetivos e requisitados, ocupantes de cargo em
comissão sem vínculo efetivo, estagiários, prestadores de serviço, colaboradores e
usuários externos com acesso aos ativos. (Mesmo universo do art. 7º da PSI nacional.)

---

## Definições próprias (art. 4º) — 34 incisos

A 974 **tem glossário próprio**, com 34 definições (incisos I a XXXIV). Consequência:
no âmbito da PSI do TRE-PR **não se depende da Portaria TSE 444/2021** para conceitos —
o que reduz a fragilidade apontada em [[normas/psi-termos-portaria-tse-444-2021]] (norma de âmbito
interno do TSE). Onde a 974 é silente, a 444 vale subsidiariamente.

**Blocos:** ameaça (I) · atividades precípuas e críticas (II-III) · ativo, ativo de
informação, ativo de processamento (IV-VI) · ciclo de vida da informação (VII) ·
cifração/decifração/recurso criptográfico (VIII, XIV, XXVII) · colaboradores (IX) ·
continuidade de negócios (X) · criticidade (XI) · custodiante (XII) · dados (XIII) ·
diretriz (XV) · disponibilidade (XVI) · documento (XVII) · gestão de riscos (XVIII) ·
gestão de segurança da informação (XIX) · incidente em redes × incidente em SI
(XX-XXI) · informação (XXII) · plano de continuidade de serviços essenciais de TI
(XXIII) · proprietário(a) da informação (XXIV) · quebra de segurança (XXV) · recurso
(XXVI) · rede de computadores (XXVIII) · risco (XXIX) · segurança da informação (XXX) ·
tratamento da informação (XXXI) · usuário externo e interno (XXXII-XXXIII) ·
vulnerabilidade (XXXIV).

### O que a 974 define DIFERENTE da Portaria TSE 444/2021
- **Custodiante (XII):** responsável pelo processamento ou armazenamento da informação
  nas tarefas de rotina **por delegação do gestor da informação**. A 444 (XIX) define
  custodiante por referência à guarda de sistema/ativo que não lhe pertence. Conceitos
  não equivalentes.
- **Proprietário(a) da informação (XXIV):** pessoa **ou setor** que **produz** a
  informação, capaz de estimar sua criticidade. A 444 (XL) fala em *proprietário do
  ativo de informação* — indivíduo instituído por posição/cargo, responsável primário
  pela viabilidade do ativo. **São figuras distintas** — atenção ao atribuir
  responsabilidade por classificação ou inventário.

### Definições que só existem na 974
criticidade (XI), dados (XIII), diretriz (XV), documento (XVII), gestão de riscos
(XVIII), **plano de continuidade de serviços essenciais de TI (XXIII)**, colaboradores
(IX), usuário externo (XXXII) e usuário interno (XXXIII).

### Lacunas do glossário local
Não define **auditabilidade** (embora seja princípio no art. 2º), nem irretratabilidade,
confidencialidade, integridade ou autenticidade — define apenas disponibilidade (XVI)
entre as propriedades. Também não define nuvem, IA, trabalho remoto, provedor de
serviços nem inteligência cibernética (os 5 temas táticos novos da PSI nacional).

> **Ciclo de vida (VII):** 6 fases — produção, recepção, organização, uso, disseminação
> e destinação. **Diverge** do art. 24 da Res. TSE 23.763/2026, que lista 11 fases.
> Prevalece o art. 24 (norma superior e posterior).

---

## Estrutura de Governança (Cap. III)

### CGSIPDP — Comitê Gestor de SI e de Proteção de Dados Pessoais (art. 7º)
Colegiado multidisciplinar. Compete: propor normas complementares e diretrizes de
classificação da informação; promover a cultura de segurança; deliberar e atuar na
gestão de riscos de segurança da informação.

### Gestor(a) de Segurança da Informação (art. 8º)
Atua de forma articulada com o CGSIPDP: propõe iniciativas tecnológicas, acompanha
gestão de vulnerabilidades e indicadores, monitora cumprimento das normas.
**Poder cautelar (§único):** pode, a qualquer tempo, **suspender temporariamente serviço
ou acesso de usuário** diante de indício de risco ou incidente de segurança cibernética,
com comunicação imediata ao **Comitê de Crises Cibernéticas** e à **Diretoria-Geral**
para decisão definitiva.

### ETIR (art. 9º)
Equipe de Tratamento e Resposta a Incidentes em Redes Computacionais e de Segurança
Cibernética. Atua na prevenção, detecção, contenção e recuperação de incidentes; comunica
situações críticas ao CGSIPDP, ao Comitê de Crises Cibernéticas e, se houver dados
pessoais, ao Encarregado de Dados.

> **Norma correlata:** o Comitê de Crises Cibernéticas e os protocolos de prevenção,
> gerenciamento e investigação de ilícitos cibernéticos foram instituídos pela
> **Res. TRE-PR 962/2025**. A 974/2026 também dialoga com a **Res. TRE-PR 932/2024**
> (Sistema de Governança da JE-PR).

---

## Deveres e Uso Aceitável (Cap. II)

### Uso dos recursos (art. 5º)
Uso estritamente institucional, sujeito a monitoramento e controle.
**Vedação expressa (§único):** proibido uso de **pendrives ou HDs externos** nas estações
de trabalho, salvo situação justificada pela chefia imediata e formalmente autorizada
pela Secretaria de TI.

### Deveres dos usuários (art. 6º)
Conhecer e zelar pela PSI; proteger informações sigilosas e pessoais; preservar sigilo
de senhas/credenciais (uso pessoal e intransferível); participar de campanhas e
treinamentos; **comunicar imediatamente** falha, vulnerabilidade ou incidente à
Secretaria de TI.

---

## Tratamento da Informação e Controles de Acesso (Cap. IV)

- **Art. 10** — Tratamento conforme confidencialidade, criticidade e temporalidade,
  respeitando LGPD e LAI.
- **Art. 11** — Controle de acesso lógico por **necessidade de saber, menor privilégio
  e segregação de funções**; direitos concedidos só para a função e revisados
  periodicamente (§1º).
- **Art. 11, §2º** — **MFA obrigatório** para acessos com privilégios administrativos,
  acesso remoto à rede (VPN) e aplicações expostas externamente, conforme viabilidade
  técnica da SECTI e regulamentação por Instrução Normativa da Diretoria-Geral.
- **Art. 12** — Informação sigilosa ou dado pessoal sensível, **em trânsito ou em
  repouso** (especialmente em dispositivos móveis e backup), deve ser protegida por
  criptografia forte.

> **🔴 Achado relevante — a norma local é MAIS RÍGIDA que a nacional.**
> O art. 12 **não tem cláusula de exceção**. Compare:
> - **Res. TSE 23.644/2021 (revogada), art. 17, p.ú.:** admitia falta de criptografia
>   quando justificada e aprovada pela gestora de riscos, pela CSI ou por normativo.
> - **Res. TSE 23.763/2026, art. 24, §3º:** mantém a mesma exceção — e o §2º deslocou
>   a criptografia para um rol de salvaguardas, sem comando categórico.
> - **Res. TRE-PR 974/2026, art. 12:** comando categórico ("deverão ser protegidos"),
>   **sem exceção prevista**, e ainda **amplia** o escopo para **dado pessoal sensível**,
>   além da informação sigilosa.
>
> Consequência: no TRE-PR, a dispensa de criptografia para informação sigilosa ou dado
> sensível **não encontra base na norma local**. Invocar o art. 24, §3º da norma
> nacional para dispensar é possível em tese (norma superior e posterior), mas é tese
> a ser fundamentada — não decorrência automática. Ponto a resolver expressamente na
> revisão de alinhamento.

---

## Continuidade de Negócios (Cap. V, art. 13)

Gestão de continuidade dos serviços essenciais de TI segue, no que couber, a **PGCN da
JE-PR**. Planos de backup, recuperação de desastres (PRD) e continuidade operacional
(PCO) **testados periodicamente**, priorizando sistemas de eleição, atendimento ao
eleitor, PJe e demais serviços críticos.

---

## Disposições Finais e Penalidades (Cap. VI)

- **Art. 14** — Descumprimento sujeita à apuração de responsabilidade, com sanções
  administrativas, civis e penais cabíveis.
- **Art. 15** — Contratos, convênios e congêneres firmados após a publicação devem
  prever cláusulas de confidencialidade e obediência à PSI e à LGPD.
- **Art. 16** — Inativação de credenciais e remoção de acessos por desligamento,
  exoneração ou fim de contrato serão regulamentadas por IN da Diretoria-Geral.
- **Art. 17** — Revisão **anual** ou diante de alteração significativa no ambiente
  tecnológico ou **no arcabouço normativo nacional**.

> **🔴 O gatilho do art. 17 JÁ DISPAROU.** A edição da Res. TSE 23.763/2026 — que
> revogou a norma nacional em que a 974 se ancora — é, por definição, "alteração
> significativa no arcabouço normativo nacional". O dever de revisar **não depende**
> do ciclo anual: está ativo desde 15/6/2026 (publicação da PSI nacional).
>
> Isso muda o enquadramento de qualquer discussão sobre cronograma: a questão não é
> *se* revisar, e sim *como sequenciar*. Separar o que independe da Estratégia Nacional
> de Cibersegurança (princípios do art. 2º, desenho CSI/Unidade de SI, os 16 temas
> táticos, art. 12) do que depende dela (indicadores, maturidade, capacitação) permite
> cumprir o gatilho sem gerar retrabalho.
- **Art. 18** — Vigência na data da publicação.

---

## Mapa de Divergências: 974/2026 (local) × 23.763/2026 (nacional)

| Tema | Res. TRE-PR 974/2026 | Res. TSE 23.763/2026 | Observação |
|------|----------------------|----------------------|------------|
| Norma nacional de referência | Ancora-se na **revogada** 23.644/2021 | É a própria norma nacional vigente | 974 precede a 23.763; desalinhada |
| Princípios | DICA + irretratabilidade + auditabilidade (art. 2º) | DICA + não repúdio (art. 3º) | Divergência expressa de rol |
| Governança | CGSIPDP (art. 7º) | CSI + Unidade de SI desvinculada da TIC (art. 17) | Modelos estruturais distintos |
| Revisão | Anual (art. 17) | Máx. 4 anos, ano não eleitoral (art. 19, I) | Ciclos diferentes |
| Estrutura normativa em níveis | Não detalha 3 níveis nem 16 temas táticos | 3 níveis; 16 temas obrigatórios (art. 9º) | Local é mais enxuta |
| Controles específicos | MFA, vedação a pendrive/HD, criptografia em repouso | Trata via normas táticas/procedimentos | Local traz regras operacionais diretas |
| Definições | Glossário próprio, 34 incisos (art. 4º) | Remete a norma apartada (art. 2º → Portaria 444/2021) | Local é autossuficiente; 444 vale subsidiariamente |
| Criptografia | Comando categórico **sem exceção** (art. 12); alcança dado pessoal sensível | Salvaguarda com exceção justificada (art. 24, §§2º-3º) | **Local mais rígida que a nacional** |
| Ciclo de vida da informação | 6 fases (art. 4º, VII) | 11 fases (art. 24) | Prevalece a nacional |
| Auditabilidade | Princípio no art. 2º, mas **excluída** do conceito de SI do art. 4º, XXX e não definida | Não é princípio | Incoerência interna da 974 |

**Regra prática:** ao analisar SI no TRE-PR, aplicar a 974/2026 como norma local
operacional, mas **sempre confrontar com a 23.763/2026**; em conflito, prevalece a
nacional, e a divergência deve ser apontada como pendência de adequação (prazo nacional:
31/12/2027).

---

## Normas correlatas do TRE-PR citadas

- **Res. TRE-PR 932/2024** — Sistema de Governança da Justiça Eleitoral do Paraná
  (cria o CGSIPDP); já alterada pela Res. 980/2026 (CGER → CGERI)
- **Res. TRE-PR 962/2025** — Comitê de Crises Cibernéticas e protocolos de prevenção,
  gerenciamento e investigação de ilícitos cibernéticos
- **Res. TRE-PR 855/2020** — Regulamentação local da LAI (já no escopo da skill)

Detalhamento da 932/2024 e da 962/2025 em [[normas/governanca-e-crises-tre-pr]].
