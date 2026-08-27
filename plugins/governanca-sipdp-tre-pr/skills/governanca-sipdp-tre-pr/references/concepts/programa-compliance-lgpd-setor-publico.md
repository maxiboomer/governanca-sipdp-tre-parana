---
title: Programa de Compliance LGPD para o Setor Público
type: concept
created: 2026-07-27
updated: 2026-07-27
tags: [lgpd, setor-publico, compliance, anpd]
status: não-aplicável
curadoria: completa
escopo: contextual
---

# Programa de Compliance LGPD para o Setor Público

Metodologia para estruturar um programa de adequação à LGPD (Lei 13.709/2018) em órgãos
públicos brasileiros, integrada às resoluções da CD/ANPD e ao Guia para o Poder Público.
Organizada em duas fases (diagnóstico e implementação), apoiada num framework documental
padronizado ([[concepts/lgpd-framework-documental]]) e num modelo de avaliação de
maturidade em 12 domínios de segurança da informação e privacidade
([[concepts/lgpd-maturidade-avaliacao]]).

Se o tratamento for de tribunal especificamente (Res. CNJ 363/2021), combinar com
[[normas/cnj-resolucao-363-2021]] e [[concepts/implementacao-cnj-363-2021]].

## Quando consultar esta página

Relevante quando o pedido envolver pelo menos um destes contextos:

1. **Estruturação do programa** — o usuário quer montar um programa de compliance LGPD do zero ou amadurecer um existente.
2. **Diagnóstico (Fase 1)** — gap analysis, mapeamento de bases de dados, ciclo de vida de dados pessoais, avaliação de maturidade.
3. **Implementação (Fase 2)** — execução dos 16 marcos do programa, redação de políticas, procedimentos e matrizes.
4. **Framework documental** — necessidade de redigir, revisar ou organizar qualquer documento da taxonomia POL/PRO/MAT/FRM/PLA.
5. **Avaliação de maturidade** — diagnóstico nos 12 domínios usando a escala 0–5.
6. **Tópicos específicos do setor público** — sanções restritas da ANPD (art. 52, §3º), encarregado em órgão público, relação com a LAI, com a Resolução CNJ 363/2021 (tribunais), regras de transparência ativa vs. proteção de dados.

Esta página cobre o setor público em geral. Se for sobre tribunais especificamente
(Resolução CNJ 363/2021), combinar com [[normas/cnj-resolucao-363-2021]] e
[[concepts/implementacao-cnj-363-2021]].

## Visão geral do framework

### As duas fases do programa

O programa é construído sequencialmente em duas fases:

- **Fase 1 — Diagnóstico (Gap Analysis):** levantamento da situação atual em 8 etapas, culminando num relatório de maturidade. Detalhes em [[concepts/lgpd-diagnostico-fase1]].
- **Fase 2 — Implementação:** execução de 16 marcos operacionais que constroem a estrutura de governança, segurança e privacidade. Detalhes em [[concepts/lgpd-implementacao-fase2]].

### Os 12 domínios de segurança da informação e privacidade

Toda a arquitetura do programa se organiza em torno destes 12 domínios. São eles que são avaliados em maturidade (Fase 1) e implementados (Fase 2):

1. Gestão da Segurança e de Riscos a Dados Pessoais
2. Organização da Segurança de Dados Pessoais
3. Gestão de Ativos de Dados Pessoais
4. Controle de Acessos a Dados Pessoais
5. Gestão da Privacidade e Proteção a Dados Pessoais
6. Segurança de Recursos Humanos
7. Gestão de Comunicações
8. Segurança Física e de TI
9. Gestão de Aquisição, Desenvolvimento e Manutenção de Sistemas
10. Gerenciamento de Incidentes de Segurança de Dados Pessoais
11. Gerenciamento de Continuidade de Negócios
12. Conformidade com a LGPD

### Pilares de segurança e privacidade (CIDAL)

Os controles do programa atendem a cinco pilares interligados:

- **Confidencialidade** — apenas usuários autorizados acessam os dados pessoais.
- **Integridade** — exatidão e completude dos dados e dos métodos de tratamento.
- **Disponibilidade** — usuários autorizados têm acesso quando necessário.
- **Autenticidade** — veracidade da autoria no consentimento e fornecimento dos dados.
- **Legalidade** — uso dos dados está em conformidade com a LGPD.

### O framework documental (taxonomia)

Todo documento do programa segue um código padronizado `TIPO_DD.NNN`, onde:

- **TIPO** indica a natureza: `POL` (Política), `PRO` (Procedimento), `MAT` (Matriz), `FRM` (Formulário), `PLA` (Plano).
- **DD** é o número do domínio (01 a 12, conforme acima).
- **NNN** é o sequencial do documento dentro do domínio.

Exemplo: `POL_05.001` = Política nº 1 do domínio 05 (Gestão da Privacidade) = Política de Proteção de Dados Pessoais.

A relação completa de documentos esperados, com finalidade e conteúdo mínimo de cada um, está em [[concepts/lgpd-framework-documental]].

## Como navegar pelos arquivos de referência

Carregue apenas o(s) arquivo(s) relevante(s) à tarefa. Não carregue tudo de uma vez — o custo de contexto é desnecessário.

| Se o pedido envolve... | Carregue |
|---|---|
| Diagnóstico, gap analysis, mapeamento de bases, ciclo de vida de dados, checklist do controlador | [[concepts/lgpd-diagnostico-fase1]] |
| Execução do programa, marcos de implementação, Privacy by Design, DPIA/RIPD, incidentes | [[concepts/lgpd-implementacao-fase2]] |
| Redação ou revisão de qualquer documento POL/PRO/MAT/FRM/PLA, classificação da informação, matriz de ativos | [[concepts/lgpd-framework-documental]] |
| Avaliação de maturidade, escala 0–5, áreas de foco (Visão/Processos/Pessoas/Tecnologia/Cultura), critérios CID para ativos | [[concepts/lgpd-maturidade-avaliacao]] |
| Sanções da ANPD ao setor público, base legal, conceitos-chave, princípios e bases legais | [[concepts/lgpd-fundamentos]] |
| Resoluções vigentes da CD/ANPD, Guia para Poder Público, RIPD oficial, canal de comunicação de incidentes, prática fiscalizatória da ANPD (caso Claro/Serasa — testes de transparência, art. 18 e encarregado), hierarquia de fontes | [[concepts/lgpd-recursos-oficiais-anpd]] |
| Sistema de IA tratando dados pessoais, decisões automatizadas (art. 20), vieses algorítmicos, RIPD para projeto de IA, modelos pré-treinados de terceiros, Privacy by Design aplicado a IA | [[concepts/lgpd-ia-governanca]] |

Para pedidos amplos ("monte o programa inteiro"), trabalhe em ordem: fundamentos → recursos oficiais ANPD → fase 1 → fase 2 → framework documental → maturidade.

**Regra de ouro:** ao redigir qualquer documento normativo do programa (POL/PRO), **sempre** consulte [[concepts/lgpd-recursos-oficiais-anpd]] para verificar se há resolução ou guia oficial específico que rege o tema, antes de aplicar o conteúdo consolidado nas demais references.

## Princípios para a redação dos documentos

Ao gerar qualquer documento do framework, siga estes princípios:

1. **Linguagem normativa, não descritiva.** Documentos POL e PRO devem usar verbos no imperativo ("deve", "fica vedado", "é obrigatório") e definir responsáveis claros.
2. **Granularidade adequada.** POL = diretriz macro; PRO = passo a passo operacional; MAT = inventário/registro; FRM = formulário preenchível; PLA = cronograma com metas.
3. **Rastreabilidade legal.** Sempre que possível, citar o artigo da LGPD que fundamenta o controle (ex.: art. 7º para bases legais, art. 38 para RIPD, art. 41 para encarregado, art. 46 para segurança).
4. **Setor público em mente.** Lembrar que o controlador é órgão público, sujeito também à LAI (Lei 12.527/2011), à Lei 8.112/1990 (servidores federais) ou estatutos correlatos, e à Lei 8.429/1992 (improbidade). A base legal típica para tratamento é "cumprimento de obrigação legal" e "execução de políticas públicas" (art. 7º, II e III; art. 23), não consentimento.
5. **Sem dados ilustrativos identificáveis.** Não usar nomes, e-mails, CPFs ou dados de pessoas reais como exemplo nos modelos.

## Princípio de cautela sobre o material-fonte

Esta skill foi consolidada a partir de material didático aplicado em um órgão público, complementado com fontes oficiais da ANPD. Durante a consolidação, foi identificado pelo menos um ponto de imprecisão no material original (sanções aplicáveis ao setor público — ver [[concepts/lgpd-fundamentos]]). Ao usar este material:

- **Fontes oficiais da ANPD são canônicas.** A página [[concepts/lgpd-recursos-oficiais-anpd]] consolida resoluções vigentes, o Guia para o Poder Público e a página oficial de RIPD, com links diretos para a versão atualizada. Em caso de conflito entre o conteúdo desta página e essas fontes, **as fontes oficiais prevalecem**.
- **Resoluções regulatórias vigentes a observar:** Res. CD/ANPD nº 1/2021, nº 2/2022, nº 4/2023, nº 15/2024, nº 18/2024, nº 19/2024 e nº 32/2026. Detalhes em [[concepts/lgpd-recursos-oficiais-anpd]].
- **Guia obrigatório para o setor público:** *Guia Orientativo sobre Tratamento de Dados Pessoais pelo Poder Público* (ANPD, versão atualizada em junho de 2023). Sintetizado em [[concepts/lgpd-recursos-oficiais-anpd]].
- **Para tribunais:** integrar com a **Resolução CNJ 363/2021**.
- **Hierarquia de fontes:** LGPD > Resoluções CD/ANPD > Guias orientativos da ANPD > Notas técnicas e enunciados > conteúdo das demais páginas desta wiki.
