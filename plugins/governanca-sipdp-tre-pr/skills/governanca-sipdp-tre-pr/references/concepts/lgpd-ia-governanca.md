---
title: IA e LGPD — Governança de Privacidade em Sistemas de Inteligência Artificial
type: concept
created: 2026-07-27
updated: 2026-07-27
tags: [lgpd, ia, governanca-ia, privacidade, setor-publico]
status: não-aplicável
curadoria: completa
escopo: contextual
---

# IA e LGPD — Governança de Privacidade em Sistemas de Inteligência Artificial

Carregue este arquivo quando o pedido envolver sistemas de IA tratando dados pessoais, decisões automatizadas, vieses algorítmicos, RIPD para projeto com componente de IA, aquisição ou desenvolvimento de sistema com modelo de ML, ou a intersecção LGPD × IA em órgão público. Para o framework geral do programa, continue usando as demais references. Este arquivo trata especificamente do **recorte de IA**, não substitui as outras.

## Paradoxo central

A inteligência artificial é simultaneamente motor de inovação no setor público e epicentro de novas preocupações com privacidade. A tensão é estrutural, não circunstancial:

- A IA precisa de **dados** para funcionar e evoluir.
- O tratamento de dados pessoais demanda **limites** para preservar direitos fundamentais.

A LGPD é o instrumento que organiza essa tensão como **governança**, não apenas controle. O programa de compliance precisa, portanto, incorporar lentes específicas de IA — não basta aplicar o mesmo procedimento usado para sistemas convencionais e esperar resultado equivalente.

## Quando o recorte de IA muda o programa

Esta seção mostra onde o restante da skill precisa de complemento quando há sistema de IA no escopo. Use-a como checklist sobre o que **acrescentar** ao processo padrão, sem reescrevê-lo.

### No mapeamento (Fase 1, Etapas 1, 2 e 6)

O inventário de tratamentos, quando há IA, precisa registrar **camadas adicionais**:

- **Dados de treinamento** — origem, base legal específica para treino (não confundir com a base legal do uso em produção), prazo de retenção do dataset, forma de descarte.
- **Dados de inferência** — o que entra no modelo em produção, o que sai, e se a saída constitui novo dado pessoal.
- **Dados de fine-tuning ou retreino contínuo** — modelos que aprendem com inputs dos usuários geram um tratamento adicional que precisa ser declarado.
- **Modelos pré-treinados de terceiros** — fornecedor é **operador LGPD** (ver seção sobre operadores abaixo).
- **Outputs do modelo** — classificações, scores, embeddings e textos gerados sobre titulares são, eles próprios, dados pessoais. Devem entrar no catálogo.

### Na avaliação de riscos (Marco 1 da Fase 2)

Riscos típicos de IA a incluir na matriz de riscos (alimenta a MAT_05.002):

| Risco | Descrição operacional |
|---|---|
| **Vieses algorítmicos** | Discriminação direta ou indireta contra grupos protegidos (raça, gênero, idade, deficiência, território). Pode violar art. 6º, IX e art. 20 da LGPD, além do art. 5º, caput da Constituição. |
| **Reidentificação via modelo** | Modelos memorizam exemplos do treino e podem emitir dados que se acreditavam anonimizados. Risco crítico para modelos treinados em dados sensíveis. |
| **Desvio de finalidade** | Uso do modelo para fim distinto do declarado na base legal — comum quando um modelo treinado para finalidade A é reaproveitado para B sem revisão. |
| **Decisão automatizada com efeito sobre o titular** | Disparador do art. 20 da LGPD; exige canal de revisão por pessoa natural. |
| **Vazamento via inferência** | *Model inversion* e *membership inference attacks* permitem deduzir dados do treino ou se uma pessoa específica estava no dataset. |
| **Alucinação com dados pessoais** | Modelos generativos podem inventar dados sobre pessoas reais — afirmações falsas que violam o art. 6º, V (qualidade dos dados) e podem causar dano moral. |
| **Opacidade / falta de explicabilidade** | Dificulta atender ao art. 20, §1º (direito à explicação da lógica) e ao princípio da transparência (art. 6º, VI). |
| **Drift do modelo** | Degradação não monitorada da acurácia ao longo do tempo, especialmente desigual entre grupos. |

Cada risco entra no mapa de calor 5x5 com sua probabilidade e impacto, conforme metodologia em [[concepts/lgpd-maturidade-avaliacao]].

### No RIPD (Marco 16 da Fase 2)

**Quando IA dispara obrigação de RIPD.** Cruzando o critério oficial da ANPD (ver [[concepts/lgpd-recursos-oficiais-anpd]] seção 4) com o universo de IA, o RIPD é praticamente sempre necessário quando há:

- Sistema de IA com **decisão unicamente automatizada** com efeito jurídico ou similar significativo sobre o titular (art. 20). Atende o critério específico "decisões automatizadas" da Res. 2/2022.
- IA em **vigilância de zonas públicas** (reconhecimento facial, biometria comportamental, análise de circulação). Atende o critério "vigilância de zonas acessíveis ao público".
- IA tratando **dados sensíveis ou de menores** (atende ao critério específico correspondente).
- Modelos baseados em **tecnologias emergentes ou inovadoras** — IA generativa, foundation models, aprendizado federado, etc. (atende ao critério "tecnologias emergentes").

Quando há IA, **assumir que o critério específico está acionado** e concentrar a análise no critério geral (larga escala / afetação significativa).

**Checklist adicional para RIPD com IA** (suplementa o conteúdo recomendado pela ANPD em [[concepts/lgpd-recursos-oficiais-anpd]]):

1. O sistema toma decisões com efeito jurídico ou similar significativo sobre o titular? Qual é o efeito concreto (negativa de serviço, aplicação de medida, classificação que altera tratamento)?
2. Há canal de revisão humana ativo? Por quem? Com qual prazo? Com poder real de reverter a decisão automatizada?
3. Como foi avaliado o viés do modelo? Em quais grupos protegidos? Quais métricas foram usadas (paridade demográfica, igualdade de oportunidade, calibração)?
4. A acurácia do modelo é homogênea entre grupos? Se não, qual a mitigação adotada e qual o gap residual aceito?
5. Sob qual base legal foram coletados os dados de treinamento? Há registro?
6. Há risco de reidentificação a partir das saídas do modelo? Foi testado? Como?
7. Como será documentada a lógica geral aplicada (art. 20, §1º) e como ela será comunicada ao titular sob demanda?
8. Há monitoramento contínuo de drift e de degradação por grupo? Qual a periodicidade?
9. Se há operador (modelo de terceiro), a cláusula contratual veda explicitamente uso dos inputs para treino do modelo do fornecedor?
10. Há transferência internacional de dados via API ou serviço em nuvem? Qual mecanismo (decisão de adequação UE/Res. 32/2026, cláusulas-padrão/Res. 19/2024, garantias específicas)?

### No Privacy by Design (transversal aos marcos)

Privacy by Design aplicado a IA acrescenta exigências aos sete princípios de Cavoukian:

- **Minimização aplicada ao dataset de treino** — não basta minimizar a coleta para o uso; o conjunto de treino deve ser o menor possível para a tarefa.
- **Anonimização robusta ANTES do treino** — com avaliação formal de risco de reidentificação (k-anonymity, l-diversity ou técnicas equivalentes). Anonimização ruim no treino contamina permanentemente o modelo.
- **Privacy-Preserving ML quando viável** — *federated learning*, *differential privacy*, *secure multi-party computation*. Não são panaceia, mas são opções concretas que devem ser avaliadas e a decisão registrada.
- **Separação rigorosa entre ambiente de treino e produção** — dados de produção não devem retornar ao treino sem nova avaliação de base legal e risco.
- **Logs de inferência com retenção mínima** — balancear utilidade para auditoria contra o princípio da necessidade.
- **Documentar a explicação da lógica ANTES do go-live** — escrever a explicação durante o desenvolvimento, não improvisar quando o primeiro titular pedir.

## Direito à revisão de decisão automatizada (art. 20)

O art. 20 da LGPD prevê o direito do titular a solicitar revisão de decisões tomadas unicamente com base em tratamento automatizado que afetem seus interesses. Para o setor público:

- O canal de revisão é **obrigatório** quando há decisão automatizada com efeito sobre o titular.
- A revisão deve ser **real**, não pro forma — pessoa qualificada, com poder de reverter, com prazo definido.
- A pessoa que revisa não pode ser a mesma que operou o sistema (independência funcional).
- A explicação da **lógica geral** aplicada (art. 20, §1º) é devida ao titular. Deve ser preparada antes da operação, não improvisada caso a caso.
- Documentar o canal de revisão no **PRO_05.001 (Solicitação do Titular)** com seção específica para revisão de decisão automatizada.
- A negativa de fornecer explicação sob alegação de segredo comercial só se aplica a fornecedor privado (art. 20, §2º); em órgão público, a transparência ativa do art. 6º da LGPD combinada com a LAI restringe muito essa exceção.

## Operadores e modelos pré-treinados de terceiros

Quando o órgão usa modelo pré-treinado de fornecedor (API de visão computacional, LLM, classificador via SaaS), o fornecedor é **operador LGPD**. Pontos críticos:

- **Cláusulas LGPD obrigatórias** no contrato (ver Fase 1, Etapa 3 em [[concepts/lgpd-diagnostico-fase1]]).
- **Vedação explícita de uso dos inputs para treino** — sem essa cláusula, os dados enviados via API podem ser reutilizados pelo fornecedor para melhorar o modelo, configurando novo tratamento sem base legal específica do controlador.
- **Verificar localização do processamento** — muitos fornecedores processam em data centers fora do Brasil. Aplicar Res. CD/ANPD nº 19/2024 (transferência internacional) e nº 32/2026 (adequação UE). Consultar [[concepts/lgpd-recursos-oficiais-anpd]].
- **Direito de auditoria** — embora difícil de exercer com grandes fornecedores, deve constar do contrato.
- **Documentação de treinamento do fornecedor** — exigir do fornecedor declaração sobre origem dos dados de treino, mitigações de viés implementadas e métricas de performance por grupo, quando aplicável.

## Integração com o framework documental

Os documentos do framework precisam acomodar o recorte de IA:

| Documento | O que acrescentar para IA |
|---|---|
| `POL_05.001` (Política de Proteção de Dados) | Seção específica de princípios para tratamento via IA: minimização do treino, vedação de uso de dados sensíveis sem base legal específica, exigência de revisão humana, monitoramento de viés. |
| `PRO_05.004` (RIPD) | Anexo com checklist de IA (10 perguntas acima). |
| `POL_09.001` (Desenvolvimento Seguro) | Requisitos para projetos com IA: *data governance* pré-treino, avaliação formal de viés, testes de reidentificação, monitoramento de drift, *model card*. |
| `MAT_03.001` (Matriz de Ativos) | Modelos de IA são ativos críticos — classificar com CID alto. Datasets de treino também. |
| `MAT_05.002` (Matriz de Riscos) | Categoria específica para riscos algorítmicos (ver tabela na seção de Avaliação de Riscos acima). |
| `PRO_05.001` (Solicitação do Titular) | Fluxo específico para revisão de decisão automatizada (art. 20). |

## Pontos específicos para o Poder Público

O setor público acumula sensibilidades quando opera IA:

- **Cumprimento de obrigação legal** e **execução de políticas públicas** são as bases legais típicas (art. 7º, II e III; art. 23). Mas isso **não dispensa** o teste de necessidade e proporcionalidade — a IA precisa ser meio adequado e menos invasivo possível para atingir a finalidade.
- **Transparência ativa** (art. 6º da LGPD + LAI) cria pressão para publicação do RIPD de sistemas de IA, mesmo sem determinação específica da ANPD pelo art. 32. Sistemas de IA com efeito sobre cidadãos têm baixa hipótese de sigilo aplicável.
- **Risco reputacional e político** específico — falhas algorítmicas no setor público viram caso público (reconhecimento facial errado, classificações injustas em programas sociais, decisões judiciais automatizadas mal calibradas).
- **Integração obrigatória com a Resolução CNJ 363/2021** quando o órgão for tribunal (ver skill `cnj-363-2021`).

## Trilha sugerida para projetos com IA

Sequência mínima ao iniciar um projeto de IA com dados pessoais em órgão público:

1. Mapear o tratamento na Etapa 1 da Fase 1 (incluindo as camadas adicionais desta reference).
2. Definir base legal explícita para treino e para produção (podem ser distintas).
3. Conduzir RIPD pleno (PRO_05.004) com o checklist de IA desta reference.
4. Aprovar plano de mitigação no Comitê de Segurança da Informação e Proteção de Dados.
5. Estabelecer monitoramento de viés e drift, com periodicidade definida (mínimo semestral).
6. Publicar versão pública do RIPD (art. 32 + LAI), salvo hipótese legítima de sigilo.
7. Operacionalizar canal de revisão humana (art. 20) antes do go-live.
8. Revalidar o RIPD a cada alteração no modelo, no dataset de treino, ou na finalidade.

---

## Proveniência deste recorte

A intersecção LGPD × IA neste arquivo foi inspirada na palestra "LGPD e IA: Riscos, Impactos e Governança na Prática" de Mariana Tomasi Keppen, que estabelece o paradoxo central (IA precisa de dados × dados demandam limites) e propõe a tríade governança = mapeamento + avaliação de risco + RIPD. O desenvolvimento técnico do recorte (lista de riscos algorítmicos, checklist específico para RIPD com IA, integração com o framework documental, considerações sobre operadores que servem modelos pré-treinados) foi expandido a partir do estado da arte em governança de IA e da regulamentação vigente da ANPD, e deve ser revisado periodicamente conforme a ANPD publicar regulamentação específica sobre IA (consultar a Agenda Regulatória vigente em [[concepts/lgpd-recursos-oficiais-anpd]]).
