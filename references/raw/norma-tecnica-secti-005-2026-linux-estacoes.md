---
title: Norma Técnica SECTI Nº 005, de 05 de agosto de 2026 — Utilização do Linux em estações de trabalho
type: fonte-normativa
fonte: TRE-PR (SECTI)
url: https://www.tre-pr.jus.br/legislacao/compilada/normas-tecnicas-da-secti/2026/norma-tecnica-ndeg-005-de-05-de-agosto-de-2026
data_publicacao: 2026-08-05
status: Vigente
tags: [secti, norma-tecnica, linux, seguranca-cibernetica, estacoes-trabalho]sha256: "307d88b15b0bd1f07946d60153c0b23946f955f165c58ff906cf1dc8e3ab38ca
sha256: 307d88b15b0bd1f07946d60153c0b23946f955f165c58ff906cf1dc8e3ab38ca
---
- Acessibilidade
  - Rybená acessibilidades adicionais
  - Rybená Libras
  - Rybená voz

Subir páginaDescer página

[](https://api.whatsapp.com/send?phone=554133308500)

[Conteúdo principal \[1\]](https://www.tre-pr.jus.br/legislacao/compilada/normas-tecnicas-da-secti/2026/norma-tecnica-ndeg-005-de-05-de-agosto-de-2026#global_statusmessage)

[Menu principal \[2\]](https://www.tre-pr.jus.br/legislacao/compilada/normas-tecnicas-da-secti/2026/norma-tecnica-ndeg-005-de-05-de-agosto-de-2026#navegacaoResposiva)

[Busca \[3\]](https://www.tre-pr.jus.br/@@search-es)

[Busca avancada \[4\]](https://www.tre-pr.jus.br/@@advanced-search)

[Pagina inicial \[5\]](https://www.tre-pr.jus.br/)

[Pagina de acessibilidade \[6\]](https://www.tre-pr.jus.br/institucional/acessibilidade)

- [Acessibilidade](https://www.tre-pr.jus.br/institucional/acessibilidade "Link: Acessibilidade")
- [Ouvidoria](https://www.tre-pr.jus.br/o-tre/ouvidoria/ouvidoria "Link: Ouvidoria")
- [Transparência e prestação de contas](https://www.tre-pr.jus.br/transparencia-e-prestacao-de-contas "Link: Transparência e prestação de contas")
- [](https://www.tre-pr.jus.br/transparencia-e-prestacao-de-contas/acesso-a-informacao/servico-de-informacoes-ao-cidadao-sic)

- Imprimir

# Página interna do portal

## Seção de conteúdo

  

[Texto consolidado](https://www.tre-pr.jus.br/legislacao/compilada/normas-tecnicas-da-secti/2026/norma-tecnica-ndeg-005-de-05-de-agosto-de-2026) [Texto compilado](https://www.tre-pr.jus.br/legislacao/compilada/normas-tecnicas-da-secti/2026/norma-tecnica-ndeg-005-de-05-de-agosto-de-2026?texto=compilado)

Tribunal Regional Eleitoral - PR

Secretaria Judiciária

Coordenadoria de Sessões

Seção de Jurisprudência e Legislação Compilada

# NORMA TÉCNICA N° 005, DE 05 DE AGOSTO DE 2026.

Estabelece os procedimentos operacionais e os requisitos de segurança para a utilização do sistema operacional Linux em estações de trabalho no âmbito da Secretaria de Tecnologia da Informação do Tribunal Regional Eleitoral do Paraná.

O SECRETÁRIO DE TECNOLOGIA DA INFORMAÇÃO, no uso de suas atribuições legais e regimentais,

CONSIDERANDO a necessidade de aprimorar a segurança cibernética e padronizar as soluções no ambiente computacional da SECTI, servindo de modelo para as demais unidades do Tribunal;

CONSIDERANDO o disposto na [Resolução n° 370/2021 do CNJ](https://atos.cnj.jus.br/atos/detalhar/3706), que institui a Estratégia Nacional de Tecnologia da Informação e Comunicação do Poder Judiciário (ENTIC-JUD);

CONSIDERANDO o disposto na [Resolução CNJ nº 335/2020](https://atos.cnj.jus.br/atos/detalhar/3496), que institui a Plataforma Digital do Poder Judiciário Brasileiro (PDPJ-Br) e determina a utilização preferencial de tecnologias com código aberto (open source);

CONSIDERANDO que a diversidade de sistemas computacionais atua como uma estratégia intrínseca de segurança, mitigando o risco de indisponibilidade geral frente a incidentes como ransomware, visto que o Linux não depende de redes de autenticação centralizadas;

CONSIDERANDO a decisão da SECTI exarada do processo SEI nº 0006246-44.2025.6.16.8000 - documento nº 0089450, que acolhe os argumentos das áreas técnicas quanto à robustez de segurança da plataforma Linux e seu impacto positivo na mitigação de erros e aumento da produtividade;

RESOLVE:

CAPÍTULO I

DO OBJETIVO E DA ABRANGÊNCIA

Art. 1º Esta Norma Técnica estabelece os padrões, os requisitos obrigatórios de segurança cibernética e as diretrizes operacionais para a utilização do sistema operacional Linux nas estações de trabalho da Secretaria de Tecnologia da Informação (SECTI).

Art. 2º O uso do sistema operacional Microsoft Windows permanece como o padrão geral da instituição. Contudo, fica autorizada, em caráter de exceção, a utilização do sistema operacional Linux nas estações de trabalho das seguintes áreas técnicas:

I - Seção de Infraestrutura de Datacenter e Servidores (SIDS);

II - Seção de Rede (SREDE).

Parágrafo único. A adoção do sistema Linux deverá ocorrer exclusivamente de forma setorial, garantindo a disseminação e a padronização das boas práticas tecnológicas dentro destas duas unidades.

Art. 3º Poderá haver extensão do uso do sistema operacional Linux a outras unidades da SECTI, mediante solicitação da unidade requisitante.

§ 1º A respectiva solicitação deverá ser formalizada e acompanhada de justificativa técnica fundamentada, evidenciando a necessidade, os benefícios operacionais e o ganho de segurança para a unidade requisitante, quando for o caso.

§ 2º A efetiva autorização para o uso nas estações de trabalho dependerá de prévia análise pelo Comitê Executivo de TI (CETI) e posterior deferimento expresso do Secretário de Tecnologia da Informação.

§ 3º O fluxo de autorização obedecerá ao rito de instrução técnica, análise de risco cibernético e decisão administrativa, devendo ser autuado em processo específico no Sistema Eletrônico de Informações (SEI).

CAPÍTULO II

DA PADRONIZAÇÃO DE DISTRIBUIÇÕES

Art. 4º A governança das plataformas autorizadas ocorrerá por meio de catálogo restrito, cabendo à Coordenadoria de Infraestrutura (COINF), em manifestação conjunta com a SIDS e a SREDE, definir e homologar as distribuições Linux padrão que serão utilizadas.

Parágrafo único. As estações Linux deverão ser obrigatoriamente cadastradas no sistema de inventário de ativos do Tribunal, com identificação clara do hardware e do responsável técnico.

Art. 5º Recomenda-se que a homologação contemple sistemas com confiabilidade corporativa e ciclos de atualização previsíveis, tais como: Ubuntu, Debian, Fedora e OpenSuse.

CAPÍTULO III

DOS REQUISITOS DE SEGURANÇA E CONFORMIDADE

Art. 6º As estações de trabalho autorizadas a utilizar o sistema Linux deverão observar rigorosamente os seguintes princípios de segurança cibernética:

I - adoção de instalação minimalista, contemplando exclusivamente os softwares e serviços estritamente necessários para o desempenho da função do usuário, a fim de reduzir a superfície de ataque;

II - gestão restrita de softwares, sendo a instalação e atualização de pacotes realizadas obrigatoriamente por meio de repositórios oficiais e assinados digitalmente;

III - manutenção de contingência imediata, preservando-se a aptidão dos computadores para operar também com o sistema Microsoft Windows (via dual-boot ou arranjo similar), resguardando o retorno rápido caso as determinações superiores inviabilizem a continuidade do uso do Linux.

Art. 7º É obrigatória a integração das estações Linux às soluções de segurança corporativas adotadas pelo Tribunal, contemplando, sempre que tecnicamente aplicável:

I - agente de monitoramento de eventos de segurança (SIEM);

II - antivírus corporativo compatível com a plataforma;

III - agente de gestão de vulnerabilidades.

Art. 8º O controle de acessos privilegiados deverá ser estritamente monitorado. Todas as credenciais administrativas deverão estar integradas à solução de cofre de senhas corporativa (CyberArk), submetendo-se ao rotacionamento obrigatório para garantir o controle e o rastreio das sessões.

CAPÍTULO IV

DAS ATRIBUIÇÕES E RESPONSABILIDADES

Art. 9º Ficam definidos os seguintes papéis e responsabilidades para a gestão deste modelo operacional:

I - Seção de Infraestrutura de Datacenter e Servidores (SIDS) e Seção de Rede (SREDE): responsáveis por implementar e documentar o uso setorial das distribuições homologadas, bem como sanear proativamente o ambiente operacional em relação a protocolos legados;

II - Assessoria de Segurança Cibernética (ASC): responsável pela governança de riscos e pela instalação de agentes de cibersegurança nas estações, o que se dará mediante o uso de credenciais específicas criadas com este propósito.

Parágrafo único - A ASC deverá elaborar e submeter à SECTI relatórios informando eventuais descumprimentos desta Norma Técnica.

CAPÍTULO V

DAS DISPOSIÇÕES FINAIS

Art. 10º Casos omissos, desafios supervenientes de interoperabilidade ou exceções técnicas deverão ser submetidos à análise do Secretário de Tecnologia da Informação.

Art. 11. Esta Norma Técnica entra em vigor na data de sua publicação.

Curitiba, 05 de Agosto de 2026.

Gilmar José Fernandes de Deus

SECRETÁRIO DE TECNOLOGIA DA INFORMAÇÃO

Este texto não substitui o publicado no [DJE-TRE-PR, nº](https://www.tre-pr.jus.br/servicos-judiciais/diario-da-justica-eletronico/diario-da-justica-eletronico-sistema) [152, de 07 de agosto de 2026, p. 10-12.](https://www.tre-pr.jus.br/servicos-judiciais/diario-da-justica-eletronico/diario-da-justica-eletronico-sistema)

### Gestor responsável

Seção de Jurisprudência e Legislação Compilada

[Aviso aos Usuários - **Emails falsos**](https://www.tre-pr.jus.br/institucional/conheca-o-tre-pr/comunicados/aviso-aos-usuarios-emails-falsos "Link: Aviso aos Usuários - <strong>Emails falsos</strong>")

## Acesso rápido

Acesso rápido

Buscar em todo site

Mapa do site

[Serviços eleitorais](https://www.tre-pr.jus.br/servicos-eleitorais)

[Eleições](https://www.tre-pr.jus.br/eleicoes)

[Partidos](https://www.tre-pr.jus.br/partidos)

[Comunicação](https://www.tre-pr.jus.br/comunicacao)

[Jurisprudência](https://www.tre-pr.jus.br/jurisprudencia)

[Legislação](https://www.tre-pr.jus.br/legislacao)

[Serviços judiciais](https://www.tre-pr.jus.br/servicos-judiciais)

[Institucional](https://www.tre-pr.jus.br/institucional)

### Política de privacidade

O Tribunal Regional Eleitoral do Paraná utiliza cookies, armazenados apenas em caráter temporário, para geração de informações estatísticas de visitação no seu portal institucional e aperfeiçoamento da experiência do usuário na utilização de serviços online, conforme nossa
**[Política de Privacidade](https://www.tre-pr.jus.br/transparencia-e-prestacao-de-contas/lei-geral-de-protecao-de-dados/politica-de-privacidade-do-tribunal-regional-eleitoral-do-parana)**
. Ao utilizar nossos serviços, você concorda com o tratamento de dados.

Aceitar todos os cookiesRejeitar cookies não necessários [Gerenciar preferências](https://www.tre-pr.jus.br/legislacao/compilada/normas-tecnicas-da-secti/2026/norma-tecnica-ndeg-005-de-05-de-agosto-de-2026#)

Usamos cookies para melhorar sua experiência, personalizar conteúdos e analisar o tráfego. Você pode gerenciar suas preferências abaixo e escolher quais categorias deseja permitir. Sua privacidade é importante para nós.

Cookies necessáriosSempre ativos

Cookies extremamente necessários são aqueles essenciais para o funcionamento do site. Eles permitem recursos básicos como navegação, login e segurança.

Cookies de desempenho

Cookies de desempenho ajudam a entender como os visitantes usam o site. Eles coletam dados anônimos sobre navegação e erros.