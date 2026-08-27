---
title: "NORMA TÉCNICA Nº 001, DE 04 DE FEVEREIRO DE 2026. — Tribunal Regional Eleitoral do Paraná"
type: fonte-normativa
source_url: "https://www.tre-pr.jus.br/legislacao/compilada/normas-tecnicas-da-secti/2026/norma-tecnica-no-01-de-04-de-fevereiro-de-2026"
coletado: 2026-08-06
tags: [tre-pr, norma, coleta-automatica]
---

NORMA TÉCNICA Nº 001, DE 04 DE FEVEREIRO DE 2026. — Tribunal Regional Eleitoral do Paraná

Acessibilidade

Rybená acessibilidades adicionais

Rybená Libras

Rybená voz

Subir página

Descer página

Conteúdo principal [1]

Menu principal [2]

Busca [3]

Busca avancada [4]

Pagina inicial [5]

Pagina de acessibilidade [6]

Acessibilidade

Ouvidoria

Transparência e prestação de contas

Imprimir

Página interna do portal
Seção de conteúdo

Compartilhar página por e-mail

Compartilhar pagina via Facebook

Compartilhar página no WhatsApp

Texto consolidado

Texto compilado

Tribunal Regional Eleitoral - PR

Secretaria Judiciária

Coordenadoria de Sessões

Seção de Jurisprudência e Legislação Compilada

NORMA TÉCNICA Nº 001, DE 04 DE FEVEREIRO DE 2026.

Estabelece os procedimentos para o Modelo Operacional de Nuvem (Cloud Operating Model), abrangendo a gestão do ciclo de vida, inventário e segurança de recursos no âmbito do Tribunal Regional Eleitoral do Paraná.

O SECRETÁRIO DE TECNOLOGIA DA INFORMAÇÃO, no uso de suas atribuições legais e regimentais,

CONSIDERANDO o disposto na Resolução n° 370/2021 do CNJ, que institui a Estratégia Nacional de Tecnologia da Informação e Comunicação do Poder Judiciário (ENTIC- JUD);

CONSIDERANDO a estratégia estratégia para uso de software e serviços de computação em nuvem, estabelecida na Portaria 257/2025 - PRES/TRE-PR;

CONSIDERANDO a necessidade de padronizar a utilização de recursos de computação em nuvem; e

CONSIDERANDO o contido no SEI nº 0001720-34.2025.6.16.8000,

RESOLVE:

CAPÍTULO I

DO OBJETIVO E DA ABRANGÊNCIA

Art. 1º Esta Norma Técnica estabelece os procedimentos obrigatórios para o planejamento, provisionamento, operação e descarte de recursos de Computação em Nuvem no âmbito do Tribunal Regional Eleitoral do Paraná.

Art. 2º São objetivos desta norma:

I - assegurar a eficiência operacional e o controle financeiro dos ativos em nuvem;

II - garantir a conformidade com as normas de Segurança da Informação e com a Lei Geral de Proteção de Dados (LGPD).

CAPÍTULO II

DAS ATRIBUIÇÕES E RESPONSABILIDADES

Art. 3º Ficam definidos os seguintes papéis e responsabilidades para a gestão do modelo operacional:

I - Requisitante de Negócio: Unidade administrativa ou judiciária solicitante, responsável funcional pela demanda, validação da solução e alinhamento com as necessidades da área;

II - Administrador de Nuvem (Técnico): Equipe técnica responsável pela execução, provisionamento, configuração, manutenção de cópias de segurança (backups) e aplicação de correções de segurança;

III - Gestor de Segurança (GSI): Responsável pela governança de riscos, definição de políticas de acesso, classificação da sensibilidade dos dados e realização de auditorias;

IV - Autoridade Aprovadora: Responsável pela gestão orçamentária e contratual, com competência para autorizar a criação de recursos que gerem custos para o Tribunal.

CAPÍTULO III

DO CICLO DE VIDA DOS RECURSOS

Art. 4º Todo recurso computacional em nuvem deve percorrer obrigatoriamente quatro estágios sequenciais, sendo vedada a criação de recursos sem formalização prévia.

Art. 5º O Estágio 1 (Planejamento e Aprovação) compreende:

I - a solicitação via preenchimento do Documento de Oficialização de Demanda pelo Requisitante;

II - a análise de viabilidade técnica e estimativa de custos mensais pelo Administrador de Nuvem;

III - a autorização formal pela Autoridade Aprovadora.

Art. 6º O Estágio 2 (Provisionamento) deve obedecer aos seguintes critérios:

I - uso de modelos de configuração pré-aprovados pela área técnica;

II - aplicação obrigatória de etiquetas (tagging) de identificação;

III - habilitação nativa de criptografia de disco e logs de auditoria.

Art. 7º O Estágio 3 (Operação e Monitoramento) consiste em:

I - gestão de vulnerabilidades com aplicação mensal de patches;

II - rotina de backup semanal automatizada para ambientes de produção (retenção mínima de 0 dias) e backup sob demanda para testes;

III - revisão mensal de faturamento para identificação de desvios financeiros.

Art. 8º O Estágio 4 (Descomissionamento) define o descarte seguro através de:

I - realização de backup final para arquivamento de longo prazo (cold storage);

II - período de quarentena de 3 (três) a 5 (cinco) dias úteis com o recurso desligado antes da exclusão;

III - exclusão lógica definitiva e cancelamento de cobranças.

CAPÍTULO IV

DA POLÍTICA DE INVENTÁRIO E ETIQUETAGEM

Art. 9º A gestão do inventário será realizada obrigatoriamente via etiquetas (tags) na plataforma ITSM adotada pelo Tribunal, conforme os padrões:

Etiqueta (Tag)

Finalidade

Centro Custo

Identificação do projeto ou departamento para rateio financeiro.

Responsável Técnico

Identificação da equipe ou servidor responsável pela manutenção.

Ambiente

Classificação em: Produção, Homologação, Desenvolvimento ou Teste.

Data Revisão

Data (MM/AAAA) para reavaliação da necessidade de manutenção do recurso.

CAPÍTULO V

DOS PROCEDIMENTOS FUNDAMENTAIS DE SEGURANÇA

Art. 10. O controle de identidade e acesso deve observar:

I - obrigatoriedade de Múltiplo Fator de Autenticação (MFA) para console de gerenciamento;

II - uso de contas nominais vinculadas a CPF, sendo vedadas contas genéricas;

III - aplicação estrita do princípio do privilégio mínimo.

Art. 11. A segurança de rede e perímetro seguirá o princípio de "Bloqueio Padrão" (Deny All), com acessos administrativos (RDP/SSH) permitidos apenas via VPN ou túneis seguros.

Art. 12. Na proteção de dados, é obrigatória a criptografia em repouso para volumes e bancos de dados, sendo vedada a cópia de dados reais com informações pessoais sensíveis para ambientes de desenvolvimento, salvo se anonimizados.

CAPÍTULO VI

DAS DISPOSIÇÕES FINAIS

Art. 13. Casos omissos ou exceções técnicas deverão ser submetidos à análise do Secretário de Tecnologia da Informação.

Art. 14. Esta Norma Técnica entra em vigor na data de sua publicação.

Curitiba, (Datado e assinado eletronicamente)

Este texto não substitui o publicado no DJE-TRE-PR, nº 037, de 02 de março de 2026, p. 16-18.

---
**Fonte:** [NORMA TÉCNICA Nº 001, DE 04 DE FEVEREIRO DE 2026. — Tribunal Regional Eleitoral do Paraná](https://www.tre-pr.jus.br/legislacao/compilada/normas-tecnicas-da-secti/2026/norma-tecnica-no-01-de-04-de-fevereiro-de-2026)
**Publicação:** DJE-TRE-PR, nº 037, de 02 de março de 2026, p. 16-18.
