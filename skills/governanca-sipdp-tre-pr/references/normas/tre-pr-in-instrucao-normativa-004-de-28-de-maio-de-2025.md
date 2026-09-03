---
title: "Instrução Normativa TRE-PR 004/2025 — Gestão de Identidade e Controle de Acesso"
name: "Instrução Normativa TRE-PR 004/2025 — Gestão de Identidade e Controle de Acesso"
created: 2026-08-31
updated: 2026-08-31
type: fonte-normativa
number: 004
year: 2025
status: vigente
curadoria: completa
escopo: central-si-pdp
status_verificacao: "Confirmada vigente em 2026-08-31: compilado oficial TRE-PR e publicação DJE-TRE-PR nº 102, 30/05/2025, p. 05-15. Texto integral coletado e revisado conforme fonte oficial."
confidence: high
fonte_publicacao: "https://www.tre-pr.jus.br/legislacao/compilada/instrucoes-normativas-tre-pr/2025/instrucao-normativa-no-004-de-28-de-maio-de-2025"
data_publicacao: "28/05/2025"
tags: [norma, tre-pr, seguranca-informacao, controle-acesso, identidade, si-pdp]
sources: [references/raw/tre-pr-in-instrucao-normativa-004-de-28-de-maio-de-2025.md]
---

# Instrução Normativa TRE-PR 004/2025 — Gestão de Identidade e Controle de Acesso

## Finalidade e escopo

Esta norma integra o corpus de **SI/PDP e governança** do TRE-PR. Institui norma de **Gestão de Identidade e Controle de Acesso Lógico e Físico** ao ambiente de Tecnologia da Informação, relativa à segurança da informação e comunicação, no âmbito da Justiça Eleitoral do Paraná. Fonte bruta preservada em `references/raw/tre-pr-in-instrucao-normativa-004-de-28-de-maio-de-2025.md`.

Aplica-se (Art. 6º) a magistrados, servidores efetivos/requisitados, ocupantes de cargo em comissão sem vínculo, estagiários, prestadores de serviço, colaboradores, usuários externos, órgãos públicos e entidades privadas contratadas/parceiras que façam uso dos ativos de TI.

## Síntese estrutural da IN

- **Art. 1º** Institui norma de Gestão de Identidade e Controle de Acesso Lógico e Físico.
- **Art. 2º** Observa a PSI da Justiça Eleitoral (Res. TSE 23.644/2021).
- **Art. 3º** Conceitos e definições (Anexo Único — 16 termos, incl. autenticação, MFA, RBAC, criptografia, VPN, token).
- **Art. 4º** Princípios do controle de acesso: necessidade de saber, necessidade de uso, privilégio mínimo, segregação de funções.
- **Art. 5º** Objetivos: estabelecer diretrizes de acesso físico/lógico; assegurar confidencialidade, integridade e disponibilidade dos ativos de TI.
- **Art. 6º** Âmbito de aplicação; §§ 1º-2º (contratos devem observar a norma; corresponsabilidade).

### Cap. V — Controle de Acesso Físico

- **Art. 7º** CGSIPDP define perímetro de segurança física para datacenter e áreas críticas.
- **Art. 8º** Diretrizes para datacenter (11 incs.): paredes sólidas, videomonitoramento, controle de acesso com registro de data/hora, autenticação, portas corta-fogo, detecção de intrusos, proteção contra ameaças ambientais, proteção contra raios, alimentação alternativa, iluminação/comunicação de emergência, controle de temperatura/umidade.
- **Art. 9º** Áreas com informações críticas fora do datacenter (diretrizes do CGSIPDP).
- **Art. 10** Proteção de equipamentos de processamento/armazenamento (4 incs.).
- **Art. 11** Segurança do cabeamento (energia e telecom).
- **Art. 12** Manutenção de equipamentos (4 incs.: pessoal autorizado, registro de falhas, eliminação de dados sensíveis, inspeção pós-manutenção).
- **Art. 13** Reutilização/descarte seguro de equipamentos (destruição física de mídias com informação restrita).

### Cap. VI — Controle de Acesso Lógico

- **Art. 14** Acesso apenas a usuário identificado e autorizado; regra "tudo proibido a menos que expressamente permitido".
- **Art. 15** Concessão/revação de acesso por processo formal; desabilitação (não exclusão) de contas para preservar trilhas de auditoria.
- **Art. 16** Padronização de nomes de usuário e e-mail.
- **Art. 17** Modelo preferencial: RBAC (controle de acesso baseado em papéis).
- **Art. 18** Inventário de contas (usuário, administrador, serviço); revisão trimestral.
- **Art. 19** Inventário de sistemas de autenticação (internos e remotos).
- **Art. 20** Gestão centralizada de contas internas via sistema de gestão de identidade.
- **Art. 21** Criação automática de usuários a partir de fontes autoritativas (SECGP para magistrados/servidores/estagiários; SECAD para colaboradores/prestadores).
- **Art. 22** Solicitação de direitos de acesso via Central de Serviços da SECTI (8 §§, incl. perfil padrão, grupos de distribuição, proibição de permissão antes de autorização formal).
- **Art. 23** Identificação única e exclusiva do usuário.
- **Art. 24** Dever da chefia de informar movimentação/desligamento; bloqueio automático após 40 dias sem acesso (incl. aposentados/cedidos).
- **Art. 25** Revisão periódica de direitos de acesso.
- **Art. 26** Registro de atividades de identidade/acesso/autenticação; relatórios críticos.
- **Art. 27** Cláusulas contratuais de sanção por acesso não autorizado.
- **Art. 28** Revisão de direitos pelo gestor do ativo (automatizável pela SECTI).

### Acesso privilegiado

- **Art. 29** Acesso privilegiado apenas a quem tem atribuição funcional de administrar; credenciais exclusivas; registro para auditoria; prazo de expiração; solicitação via processo administrativo ao Secretário de TI para unidades não-gestoras.
- **Art. 30** Avaliação mensal de competências de acesso privilegiado.
- **Art. 31** Evitar identidade de administrador genérico; se inevitável, troca periódica de senha e auditoria.
- **Art. 32** Acesso privilegiado via ferramenta de controle de acesso privilegiado (unidade de segurança cibernética).
- **Art. 33** MFA para login de usuários da SECTI em estações de trabalho.

### Política de senhas

- **Art. 34** Restrição de acesso via senha/token; MFA para remoto/administrativo/externo.
- **Art. 35** Uso pessoal e intransferível.
- **Art. 36** Requisitos de senha (8+ chars com MFA, 14+ chars sem MFA; complexidade; modificação de senha temporária; não expor).
- **Art. 37** Não reutilizar credenciais pessoais/profissionais.
- **Art. 38** Alterar senha em caso de comprometimento.
- **Art. 39** Requisitos do sistema de gerenciamento de senha (10 incs.: seleção pelo usuário, troca trimestral, histórico, criptografia, hash com salt, não exibir na tela, etc.).
- **Art. 40** Emissão de senha temporária (vedada a emissão para ciência de terceiros ou envio em texto claro).

### Procedimentos seguros de login

- **Art. 41** Recomendações de login (7 incs.): sem mensagens de ajuda, validação após preenchimento completo, não indicar qual dado está errado, bloqueio após 5 tentativas, registro de tentativas, exibir último acesso, encerramento de sessão inativa após 30 min.

### Acesso à rede

- **Art. 42** Regra "tudo proibido a não ser que expressamente permitido" para dispositivos/serviços de rede.
- **Art. 43** Autorização de novo equipamento via chamado na Central de Serviços.
- **Art. 44** Redes do TRE-PR (cabeada, wi-fi, VPN, Internet, zonas eleitorais).
- **Art. 45** Vedada inclusão de equipamentos pessoais em redes internas sem autorização.
- **Art. 46** Horário de VPN/Internet regulamentado em portaria; alterações excepcionais ao Comitê de SI.
- **Art. 47** Inclusão em VPN via processo administrativo.
- **Art. 48** Registro de acessos à rede (mínimo 3 meses) e relatórios críticos.
- **Art. 49** MFA opcional para máquinas na VPN.
- **Art. 50** Remover (não apenas desabilitar) serviços de rede em desuso.

### Código-fonte

- **Art. 51** Acesso ao código-fonte restrito a quem tem atribuição funcional; armazenamento em ferramentas apropriadas; registro de eventos de acesso.

### Disposições finais

- **Art. 52** Casos omissos resolvidos pela SECTI ou CGSIPDP.
- **Art. 53** Revisão pelo Gestor de SI quando necessário.
- **Art. 54** Descumprimento sujeito a apuração e penalidades.
- **Art. 55** Vigência a partir da publicação (DJE-TRE-PR nº 102, 30/05/2025, p. 05-15).

## Fundamentos normativos

Res. CNJ 370/2021 (ENTIC-JUD), Res. CNJ 396/2021 (ENSEC-PJ), Res. TSE 23.644/2021 (PSI), **Res. TRE-PR 940/2024** (Código de Ética e Integridade), IN GSI/PR 01/2008, Norma Complementar 07/IN01/DSIC/GSIPR, ABNT NBR ISO/IEC 27001/27002/27005/27701, Acórdão TCU 1.603/2008.

## Status normativo

**Vigente** — confirmada em 2026-08-31 (compilado oficial TRE-PR + DJE-TRE-PR nº 102, 30/05/2025, p. 05-15).

- Publicação: DJE-TRE-PR nº 102, 30/05/2025, p. 05-15.
- Norma operacional de SI/PDP: estabelece controles de acesso físico e lógico, alinhada à PSI-JE.
- **Cita como fundamento** a Res. TRE-PR 940/2024 (Código de Ética e Integridade).

## Relações

- [[references/concepts/seguranca-informacao-justica-eleitoral]]
- [[references/entities/cgsipdp]]
- [[references/entities/secti]]
- [[references/normas/tre-pr-resolucao-940-2024]]
- [[references/normas/psi-tse-23644-2021-revogada]]

## Fonte integral

- `references/raw/tre-pr-in-instrucao-normativa-004-de-28-de-maio-de-2025.md`
- Publicação/URL registrada: https://www.tre-pr.jus.br/legislacao/compilada/instrucoes-normativas-tre-pr/2025/instrucao-normativa-no-004-de-28-de-maio-de-2025

## Nota de qualidade

Página criada em 2026-08-31 e revisada no mesmo dia para refletir a estrutura real da IN (55 artigos). Não constitui certificação de vigência: o campo `status_verificacao` explicita a pendência de confirmação oficial de curadoria.
