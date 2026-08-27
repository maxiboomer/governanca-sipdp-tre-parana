---
title: Monitoramento de Normas Internas (SECTI / TRE-PR)
type: concept
created: 2026-07-27
updated: 2026-07-27
tags: [secti, tre-pr, cnj, inventario-normas, tecnologia-informacao]
status: não-aplicável
curadoria: completa
escopo: contextual
---

# Monitoramento de Normas Internas (SECTI / TRE-PR)

Consulta e mantém o inventário de normas internas de TI e Segurança da Informação do
TRE-PR (Resoluções, Portarias, IN-DG, Normas Técnicas SECTI, Ordens de Serviço) e normas
correlatas do CNJ, com status de vigência (Vigente/Revogada/Em revisão). Consultar sempre
que for preciso saber se uma norma, IN, Portaria, Resolução ou Norma Técnica SECTI está
vigente, localizar a norma de um processo de TI (mudanças, incidentes, capacidade,
ativos, contratações, criptografia, backup, ETIR, Comitê de Gestão da TI), ou atualizar
o inventário. As tabelas completas estão em [[inventarios/normas-tre-pr-tse]] e
[[inventarios/normas-cnj]].

Esta página mantém e consulta o inventário de normas de TI e Segurança da
Informação do TRE-PR mantido pela SECTI (Secretaria de Tecnologia da
Informação), cruzado com as normas correlatas do CNJ.

## Escopo x [[concepts/seguranca-informacao-justica-eleitoral]]

Esta página é o **inventário factual** (o que existe, qual o status de
vigência, qual a ementa, onde foi publicado). Para **interpretação jurídica
aprofundada** de PSI, LAI, PGPPDP, governança e crises cibernéticas — prazos,
competências, estrutura de governança, pareceres de conformidade — use
[[concepts/seguranca-informacao-justica-eleitoral]], que é complementar a esta. Ao
responder qualquer pergunta sobre PSI (Res. TSE 23.763/2026 ou Res. TRE-PR 974/2026),
GSI, ETIR, CGSIPDP, PGPPDP ou LAI, consulte também aquela página
— não pare só no inventário.

## Arquivos de referência

- [[inventarios/normas-tre-pr-tse]] — inventário completo de normas do TRE-PR (e do
  TSE quando aplicável), colunas: Norma, Procedência, Ementa, Situação da
  norma, 1ª versão, Última revisão, Situação (fonte/publicação), Observações.
- [[inventarios/normas-cnj]] — inventário de normas do CNJ relevantes para
  TIC/SI aplicáveis ao TRE-PR, agrupadas por eixo temático (Governança e
  Gestão de TIC, Inteligência Artificial e Inovação, Segurança da Informação e
  Proteção de Dados, Soluções de TIC e Plataformas).

Sempre releia o arquivo de referência relevante antes de responder — não
responda de memória mesmo que a norma pareça familiar de uma consulta
anterior nesta conversa, porque o inventário pode ter sido atualizado.

## Como responder

### 1. Consulta factual direta
("A IN-DG 04/2020 está vigente?", "quem edita a Norma Técnica SECTI 02/2026?")
- Localize a linha exata em [[inventarios/normas-tre-pr-tse]] ou [[inventarios/normas-cnj]].
- Responda com Norma, Situação da norma e, se houver, a coluna Observações
  (ela carrega alertas e correções importantes — nunca ignore).
- Se a norma tiver sido revogada, informe pelo que foi revogada, quando
  disponível.

### 2. Localizar norma por processo/tema
("Qual norma trata de gerenciamento de mudanças de TI?", "onde está a
regulamentação de backup?")
- Busque por palavras-chave na coluna Ementa.
- Se houver mais de uma norma no mesmo tema (comum em Normas Técnicas SECTI
  que se sucedem por ano), liste todas e destaque qual está **Vigente**.

### 3. Checagem de vigência antes de qualquer uso formal
Antes de citar uma norma como base para um parecer, um e-mail institucional ou
qualquer entrega ao usuário, **sempre confira a coluna "Situação da norma"**.
Nunca afirme que algo é vigente só porque é o nome mais conhecido ou mais
citado — várias normas revogadas na tabela seguem sendo mencionadas
informalmente pelo nome antigo (ex.: a extinta Res. TSE 23.644/2021, hoje
substituída pela Res. TSE 23.763/2026).

### 4. Atualização do inventário
Quando o usuário informar uma norma nova, uma revogação, ou pedir para
"atualizar a planilha"/"atualizar o inventário":
1. Pergunte (ou confirme, se já estiver claro na conversa) os campos: Norma,
   Procedência, Ementa, Situação da norma, 1ª versão, Última revisão,
   Situação/fonte de publicação.
2. Edite [[inventarios/normas-tre-pr-tse]] ou [[inventarios/normas-cnj]] mantendo o formato de
   tabela existente — não reordene colunas.
3. Se a norma corrigir ou revogar outra já listada, atualize também a
   "Situação da norma" da norma antiga e registre em Observações a razão e a
   data da correção (padrão: `CORREÇÃO (DD/MM/AAAA): ...` ou `ADICIONADA
   (DD/MM/AAAA): ...`).
4. Se o usuário mantém a planilha `.xlsx` original (SECTI - Monitoramento de
   normas), ofereça também atualizar o arquivo Excel diretamente — use a
   skill `xlsx` para isso, replicando as mesmas colunas e sem alterar
   formatação de linhas não tocadas.

### 5. Alertas de nomenclatura (não repetir o erro já corrigido)
Dois pontos de confusão já identificados e documentados em Observações — não
os reintroduza ao responder:
- **"Gestor de Sistema Informatizado"** (IN-DG nº 04/2020) é papel distinto de
  **"Gestor de Segurança da Informação — GSI"** (Res. TSE 23.763/2026, art.
  17, III). O primeiro é dono funcional de um sistema; o segundo é o titular
  da Unidade de SI, subordinado à alta administração. Nunca cite a IN-DG
  04/2020 como evidência de que o GSI institucional está regulamentado.
- **Res. TSE 23.644/2021** aparece revogada no inventário — se o usuário
  perguntar por ela citando-a como se estivesse vigente, corrija e aponte
  para a Res. TSE 23.763/2026.

## Estrutura de resposta

Para perguntas simples, responda direto, sem preâmbulo:
> **[Norma]** — [Situação da norma]. [Ementa resumida]. [Observação relevante,
> se houver].

Para pedidos de levantamento por tema, use tabela quando houver 3+ resultados
relevantes: Norma | Situação | Ementa | Observações.

Para atualizações, sempre confirme com o usuário o que foi alterado antes de
salvar, mostrando um resumo tipo diff (o que mudou, o que foi adicionado).
