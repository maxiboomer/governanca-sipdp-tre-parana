---
title: "INSTRUÇÃO NORMATIVA Nº 003, DE 31 DE AGOSTO DE 2022. — Tribunal Regional Eleitoral do Paraná"
type: fonte-normativa
source_url: "https://www.tre-pr.jus.br/legislacao/compilada/instrucoes-normativas-tre-pr/2022/instrucao-normativa-no-003-de-31-de-agosto-de-2022"
coletado: 2026-08-06
tags: [tre-pr, norma, coleta-automatica]
---

INSTRUÇÃO NORMATIVA Nº 003, DE 31 DE AGOSTO DE 2022. — Tribunal Regional Eleitoral do Paraná

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

INSTRUÇÃO NORMATIVA Nº 003, DE 31 DE AGOSTO DE 2022.

Dispõe sobre as regras e os procedimentos para a realização da gestão e monitoramento de registro de atividades (logs) no ambiente computacional da Justiça Eleitoral do Paraná.

O DIRETOR-GERAL DA SECRETARIA DO TRIBUNAL REGIONAL ELEITORAL DO PARANÁ, no uso das atribuições que lhe são conferidas pelo inciso VII do art. 29 do Regulamento da Secretaria (Resolução TRE-PR nº 878/2021),

CONSIDERANDO a necessidade de aprimorar a gestão do processo de tratamento e resposta a incidentes em redes computacionais no TRE-PR;

CONSIDERANDO a necessidade de definir processos para o gerenciamento e o monitoramento de logs (registro de eventos) em sistemas computacionais;

CONSIDERANDO a Resolução CNJ nº 396/2021, que institui a Estratégia Nacional de Segurança Cibernética do Poder Judiciário (ENSEC-PJ);

CONSIDERANDO a Resolução TSE nº 23.644/2021, que institui a Política de Segurança da Informação (PSI) no âmbito da Justiça Eleitoral;

CONSIDERANDO a Portaria DG/TSE nº 444/2021, que dispõe sobre a instituição da norma de termos e definições relativa à Política de Segurança da Informação do Tribunal Superior Eleitoral;

CONSIDERANDO as boas práticas em segurança da informação previstas nas normas ABNT ISO/IEC 27001 e ABNT NBR ISO/IEC 27002;

CONSIDERANDO as boas práticas em segurança da informação previstas no modelo CIS Controls V.8;

CONSIDERANDO que a segurança da informação e a proteção de dados pessoais são condições essenciais para a prestação dos serviços jurisdicionais e administrativos do Tribunal Regional Eleitoral do Paraná; e,

CONSIDERANDO o contido no PAD nº 26038/2022,

RESOLVE

CAPÍTULO I

DAS DISPOSIÇÕES PRELIMINARES

Art. 1º A presente norma institui e regulamenta a gestão e monitoramento de registro de atividades (logs) no âmbito da Justiça Eleitoral do Paraná.

CAPÍTULO II

DAS DEFINIÇÕES

Art. 2º Para efeitos desta norma, consideram-se os termos e definições previstos na Portaria DG/TSE nº 444/2021, além dos seguintes:

I - Serviços de DHCP (Dynamic host configuration protocol) - servidores que fornecem endereços IP e outras configurações de forma dinâmica para o ambiente de rede de computadores;

II - Serviços de DNS (Domain name system) - servidores que fazem localização e tradução de nomes de hosts e serviços de rede para números de endereços IP;

III - SIEM - Security information event management - solução de software que faz a centralização de eventos de rede e de sistemas, com capacidade para busca e correlação entre esses eventos, possibilitando o monitoramento por parte das equipes de segurança e outros administradores de rede;

IV - SOAR - Security orchestration, automation and response - possui as mesmas funções do SIEM, com capacidade adicional de abertura de chamados e automação da resposta ao incidente, como bloqueio de usuários e geração de regras de firewall.

CAPÍTULO III

DO REGISTRO DE EVENTOS (LOGS)

Art. 3º Devem ser monitorados, com registro centralizado de logs em servidores específicos, no mínimo, os seguintes tipos de ativos em produção:

I - servidores web;

II - servidores de arquivos;

III - servidores de bancos de dados;

IV - servidores de e-mails;

V - servidores de aplicação;

VI - firewalls de rede;

VII- firewalls de aplicação;

VIII - roteadores de acesso à internet e às redes da Justiça Eleitoral;

IX - switches e roteadores de núcleo de rede (core);

X - servidores controladores de domínio e demais serviços de autenticação;

XI - serviços de gerenciamento de backups (cópias de segurança);

XII - serviços de gerenciamento de infraestrutura de virtualização e conteinerização, incluídas as baseadas em nuvem pública;

XIII - soluções anti-malware;

XIV - soluções controle de acesso físico e lógico;

XV -soluções gerais de cibersegurança;

XVI - serviços de DHCP;

XVII - serviços de DNS.

Art. 4º Os registros de eventos devem conter informações mínimas e relevantes, especialmente:

I - identificação do usuário que acessou o recurso;

II - natureza do evento, como sucesso ou falha de autenticação, tentativa de troca de senha, entre outros;

III - carimbo de tempo (timestamp), formado por data, hora e fuso horário;

IV - endereço IP (Internet Protocol), identificador do ativo de processamento, coordenadas geográficas, se disponíveis, e outras informações que permitam identificar a possível origem e destino do evento;

V - recursos acessados e seus respectivos tipos de acesso;

VI - alarmes provocados pelos sistemas de controle de acesso;

VII - informações de falhas nas aplicações ou recursos acessados;

VIII - outras informações que permitam identificar a possível origem e destino do evento.

Art. 5º Os ativos de processamento que não permitam os registros de eventos conforme indicado, ou que estejam em ambiente seguro de nuvem administrado por terceiros, devem ser mapeados e documentados quanto ao tipo e formato de registro de eventos que o sistema permite armazenar, a temporalidade do armazenamento, assim como o nível de segurança obtido.

Art. 6º Os registros de eventos devem ser armazenados na rede corporativa pelo período de 180 (cento e oitenta) dias e em cópias de segurança por um período de 12 (doze) meses, sem prejuízo de outros prazos previstos em referências legais e normativos específicos.

Art. 7º Os ativos de processamento em produção devem ser configurados de forma a gerar registros de eventos relevantes que afetem a segurança da informação, armazenando-os para utilização posterior, incluindo:

I - acesso remoto à rede corporativa;

II - autenticação, tanto as bem-sucedidas quanto as malsucedidas;

III - criação, alteração e remoção de usuários, perfis e grupos privilegiados;

IV - uso de privilégios;

V - troca de senhas;

VI - modificações de política de senhas, como tamanho, tempo de expiração, bloqueio automático após exceder determinado número de tentativas de autenticação, histórico, entre outras;
VII - acesso ou modificação de arquivos, serviços e sistemas de informação considerados críticos;

VIII - alterações na configuração de sistemas operacionais de servidores, serviços e sistemas de informação;

IX - inicialização, suspensão e reinicialização de serviços;

X - uso de aplicativos e utilitários do sistema operacional de servidores;

XI - ativação e desativação dos sistemas de proteção, como sistemas de antivírus e sistemas de detecção e prevenção de intrusos;

XII - acesso físico por senha, cartão inteligente ou biometria em área de segurança com ativos de processamento críticos como Data-Center, salas de telecomunicações, dentre outros;

XIII - acoplamento e desacoplamento de dispositivos de hardware, com especial atenção para mídias removíveis em servidores;

XIV - acesso e alteração nos registros de eventos (logs).

Art. 8º O monitoramento deve ser realizado, preferencialmente, com a utilização de ferramentas automatizadas que gerem alarmes imediatos de eventos críticos e permitam a correlação e análise dos registros de eventos gravados (SIEM/SOAR).

§ 1º O monitoramento deve ser realizado de forma a manter inalterada a rotina de trabalho do ambiente de produção.

§ 2º O nível de monitoramento pode ser reduzido em função da implementação de controles de acesso que minimizem o risco aos ativos de processamento e reduzam a exposição da informação a acessos indevidos.

§ 3º As ferramentas automatizadas devem ser analisadas criticamente em intervalos regulares para ajuste de configuração, de forma a melhorar a identificação de registros de eventos relevantes, falsos negativos e falsos positivos.

§ 4º Os processos de monitoramento devem ser revisados na implantação ou manutenção dos ativos de processamento, a fim de manter sua adequação às mudanças ocorridas.

§ 5º Os administradores devem monitorar os registros impedindo o armazenamento indevido de dados pessoais.

Art. 9º Os usuários devem estar cientes de que os ativos de processamento estão suscetíveis a monitoramento e auditoria a qualquer momento, bem como, quando houver suspeita ou constatação de uma falha de segurança.

Art. 10. Todos os eventos contrários ao ordenamento jurídico em vigor e às normas constantes da Política de Segurança da Informação, inclusive os discriminados nos incisos deste artigo, devem ser registrados formalmente e analisados, adotando-se as ações apropriadas para sua correção:

I - divulgação não autorizada de dado ou informação sigilosa contida em sistema, arquivo ou base de dados da Administração Pública, nos termos do art. 153, § 1º-A do Código Penal;

II - invasão de dispositivo informático, nos termos do art. 154-A do Código Penal;

III - interrupção de serviço telemático ou de informação de utilidade pública, previsto no § 1º do art. 266 do Código Penal;

IV - inserção ou facilitação de inserção de dados falsos, alteração ou exclusão de dados corretos nos sistemas informatizados ou bancos de dados da Administração Pública, nos termos do art. 313-A do Código Penal;

V - modificação ou alteração por agente público de sistema de informação ou programa de informática sem autorização, nos termos do art. 313-B do Código Penal;

VI - distribuição, armazenamento ou conduta vinculada a pornografia infantil, nos termos dos arts. 240, 241, 241-A, 241-B, 241-C e 241-D da Lei nº 8.069/90;

VII - interceptação telemática clandestina, nos termos do art. 10 da Lei nº 9.296/96.

CAPÍTULO IV

DA PROTEÇÃO DAS INFORMAÇÕES DOS REGISTROS DE EVENTOS
Art. 11. Os arquivos de registros de eventos devem ser protegidos para que não estejam sujeitos a falsificação ou ao acesso não autorizado às informações registradas.

Parágrafo único. A fim de assegurar a proteção de que trata o caput deste artigo, os seguintes controles mínimos devem ser implementados:

I - armazenamento, no mínimo, em 2 (dois) registros de mesmo conteúdo, protegidos contra acessos indevidos e adulteração, considerando-se ainda que ao menos destes registros esteja em local centralizado e que se consiga manter o prazo de armazenamento previsto no art. 6º;

II - guarda da cópia em segmento isolado da rede corporativa, com proteção de dispositivos de segurança suficientes para a proteção da sua integridade;

III - espaço de armazenamento adequado e alertas preventivos de seu esgotamento;

IV - localização física em área sujeita a controles de segurança;

V - emprego de protocolos seguros para acesso remoto;

VI - capacidade de assinatura digital ou resumo criptográfico para verificar a integridade;

VII - possibilidade de execução de auditorias legais e forenses;

VIII - fornecimento, para efeito de investigação, de cópia das informações relevantes, exceto nas hipóteses legais que exijam a apresentação da mídia original;

IX - geração de registros de eventos (logs) para todos os trabalhos executados nos arquivos;

X - conservação de documentação atualizada dos procedimentos de:

a) configuração, instalação e manutenção;

b) administração e operação;

c) cópia de segurança e restauração.

CAPÍTULO V

DOS REGISTROS DE EVENTOS DE ADMINISTRADOR E OPERADOR

Art. 12. Os registros de eventos de administradores e operadores com privilégios para ações e comandos especiais na rede corporativa, como super usuários, administradores de rede, entre outros, devem ter mecanismos adicionais de gerenciamento e monitoramento, considerando, no mínimo, os seguintes aspectos:

I - os registros de eventos dos administradores e operadores da rede corporativa devem ser protegidos e analisados criticamente, em intervalos regulares;

II - os administradores e operadores da rede corporativa não devem, preferencialmente, fazer parte da equipe de monitoramento e análise crítica de suas próprias atividades, respeitando o princípio da segregação de funções;

III - os administradores e operadores da rede corporativa não devem ter permissão para apagar,

alterar ou desativar os registros de eventos de suas próprias atividades.

Art. 13. Um sistema de detecção e prevenção de intrusões gerenciado fora do controle dos administradores e operadores da rede corporativa pode ser utilizado para monitorar as atividades nos registros de eventos.

CAPÍTULO VI

DA SINCRONIZAÇÃO DOS RELÓGIOS

Art. 14. O horário dos ativos de processamento deve ser ajustado por meio de mecanismos de sincronização de tempo (servidor NTP), de forma que as configurações de data, hora e fuso horário do relógio interno estejam sincronizados com a "Hora Legal Brasileira (HLB)", de acordo com o serviço oferecido e assegurado pelo Observatório Nacional - ON.

Art. 15. O estabelecimento correto dos relógios nos ativos de processamento da rede corporativa deve assegurar a exatidão dos registros de eventos, que podem ser requeridos para investigações ou como evidências em casos legais ou disciplinares, devendo atender, no mínimo, à seguinte rotina:

I - Usar fontes de tempo sincronizadas para todos os ativos monitorados, a partir das quais os ativos de processamento recuperem regularmente as informações de data, hora e fuso horário, de forma que os registros de eventos (logs) sejam cronologicamente consistentes.

CAPÍTULO VII

DISPOSIÇÕES FINAIS

Art. 16. A SECTI elaborará, em até 120 (cento e vinte dias) dias, os procedimentos operacionais para aplicação desta norma, que levem em conta as boas práticas de cibersegurança e os recursos tecnológicos disponíveis.

Art. 17. Qualquer descumprimento desta norma deve ser imediatamente comunicado e registrado como incidente de segurança da informação, para apuração pelo Comitê Gestor de Segurança da Informação, com consequente adoção das providências cabíveis.

Art. 18. Esta norma complementar deve ser revisada a cada 12 (doze) meses, ou antes, caso necessário, pelo Gestor de Segurança da Informação e encaminhada para apreciação do Comitê Gestor de Segurança da Informação.

Art. 19. Os casos omissos serão resolvidos pelo Comitê Gestor de Segurança da Informação -CGSI.

Art. 20. Esta instrução normativa entra em vigor na data de sua publicação.

Curitiba, em 31 de agosto de 2022.

VALCIR MOMBACH

Diretor-Geral do TRE-PR

Este texto não substitui o publicado no DJE-TRE-PR, nº 211, de 15 de setembro de 2022, p. 6-11.

---
**Fonte:** [INSTRUÇÃO NORMATIVA Nº 003, DE 31 DE AGOSTO DE 2022. — Tribunal Regional Eleitoral do Paraná](https://www.tre-pr.jus.br/legislacao/compilada/instrucoes-normativas-tre-pr/2022/instrucao-normativa-no-003-de-31-de-agosto-de-2022)
**Publicação:** DJE-TRE-PR, nº 211, de 15 de setembro de 2022, p. 6-11.
