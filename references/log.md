# Log

Append-only chronological record of ingests, queries, and lint passes. See `CLAUDE.md` for format.

## [2026-07-29] setup
Initialized the wiki structure inside the Obsidian vault (`raw/`, `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, `index.md`, `log.md`, `CLAUDE.md`) per the pattern described in `../llm-wiki.md`, and removed the default Obsidian welcome note. Added a Claude Code skill (`.claude/skills/llm-wiki/`) to route ingest/query/lint requests. No sources ingested yet.

## [2026-07-29] ingest | Reorganização de conteúdo pré-existente (normas eleitorais + LGPD)
Found four ad-hoc Claude Code "Skill" folders already inside the vault (`analise-normas-eleitorais/`, `cnj-363-2021/`, `lgpd-compliance-setor-publico/`, `monitoramento-normas-secti/` — each with a `SKILL.md` + `references/`)), containing a substantial, previously-audited legal knowledge base on TRE-PR/TSE information security, LGPD, LAI, and AI governance. Reorganized all of it into the wiki schema instead of leaving it in Skill-folder format:

- Added two domain-specific categories to `CLAUDE.md` (`wiki/normas/`, `wiki/inventarios/`) since this legal/regulatory corpus didn't fit cleanly into entities/concepts.
- Touched: `wiki/normas/*` (10 pages — one per legal instrument, plus an audit changelog), `wiki/concepts/*` (12 pages — hubs, methodology, cross-references), `wiki/inventarios/*` (2 raw vigency tables), `wiki/entities/*` (5 new stub pages: CGSIPDP, ETIR, CSI/Unidade de SI, Encarregado/DPO, ANPD).
- All content relocated with frontmatter added and cross-references converted from Skill-style `references/x.md` mentions to `[[wikilinks]]`; legal/regulatory prose preserved verbatim (mechanical moves + link rewrites, not rewritten by hand) to avoid corrupting a corpus that had already been carefully audited against official texts.
- Removed the emptied Skill-folder shells and a stray `sources/z.md` artifact (leftover from an illustrative example in `CLAUDE.md`, not real content).
Notes: this corpus is Portuguese-language and TRE-PR/TSE-specific — future ingests on Brazilian electoral/judicial IT law or LGPD compliance should check `[[concepts/seguranca-informacao-justica-eleitoral]]` and `[[concepts/programa-compliance-lgpd-setor-publico]]` first before creating new pages, to avoid duplicating what's already there.

## [2026-08-04] obsidian-integration

### Skill Installations Completas
- obsidian (builtin) — Read, search, create, and edit notes in Obsidian vault
- llmm-wiki (local) — Specialized workflow for llmm-wiki knowledge base
- Atualizada skill obsidian com path do llmm-wiki

### MCP Server Installation
- Instalado plugin "Local REST API with MCP" (versão 5.1.0)
- Localizado em: /c/Users/CASA/llmwiki/llm-wiki/.obsidian/plugins/obsidian-local-rest-api/
- URL: https://github.com/coddingtonbear/obsidian-local-rest-api
- Autor: Adam Coddington

### Configuration
- Vault path configurado: /c/Users/CASA/llmwiki/llm-wiki/
- Estrutura de diretórios confirmada: raw/, wiki/entities/, wiki/concepts/, wiki/normas/, wiki/inventarios/
- Workflow quick reference criado em skills/note-taking/obsidian/llmm-wiki-workflow.md

### Próximos Passos
- Ativar plugin no Obsidian: Settings > Community Plugins > Safe Mode desativado > Instalar plugin > "Local REST API with MCP"
- Configurar API key para MCP server (se necessário)
- Testar integração MCP com Hermes Agent

## [2026-08-05] ingest | Protocolo de Crise Socioambiental do TRE-PR (Portaria 056/2026)

### Norma principal criada
- **[[wiki/normas/portaria-tre-pr-056-2026.md]]** — Portaria 056/2026: Protocolo de Crise Socioambiental do TRE-PR (19/02/2026)

### Normas referenciadas criadas/atualizadas

1. **[[wiki/normas/cnj-resolucao-325-2020.md]]** — Estratégia Nacional do Poder Judiciário 2021-2026 (fundamentação para gestão de riscos)

2. **[[wiki/normas/cnj-resolucao-433-2021.md]]** — Política Nacional do Poder Judiciário para o Clima e Meio Ambiente

3. **[[wiki/normas/cnj-resolucao-646-2025.md]]** — Protocolo de Crise Socioambiental do Poder Judiciário (modelo nacional)

4. **[[wiki/normas/psi-tse-23644-2021-revogada.md]]** — Registro da norma revogada (TSE 23.644/2021), substituída pela 23.763/2026

5. **[[wiki/normas/portaria-tre-pr-302-2025.md]]** — PGCN, com notas sobre alteração pela Portaria 056/2026

### Correção de numeração (aplicada)

**Problema identificado:** Na primeira versão, citei a portaria como "Res. 303/2025".

**Correção aplicada:**
- **Portaria 056/2026** é o número oficial da norma que institui o Protocolo de Crise Socioambiental (publicada em 19/02/2026)
- O número "303/2025" era um erro aparentemente de transcrição/repetição no texto original
- Todo o vault foi revisado e atualizado para usar o nome correto

**Arquivos corrigidos:**
- `[[wiki/normas/portaria-tre-pr-056-2026.md]]` — Criado com nome correto
- `[[wiki/normas/portaria-tre-pr-302-2025.md]]` — Referências atualizadas para 056/2026
- Renomeados: `cnpj-resolucao-*.md` → `cnj-resolucao-*.md` (3 arquivos)

### Index atualizado
- Adicionadas todas as novas normas em `[[index.md]]` em seção "Protocolo de Crise Socioambiental e Continuidade"
- Criada nova seção "Segurança da Informação e Cibernética"

### Pontos críticos identificados

**⚠️ Desconsideração de norma revogada:** A Portaria 056/2026 menciona a TSE 23.644/2021, revogada em 09/06/2026, **4 meses após** sua publicação (19/02/2026). Esta inconsistência histórica é relevante para análise de primeiro grau.

**⚠️ Alteração da PGCN:** A Portaria 056/2026 altera a Portaria 302/2025, incluindo o PCSA como item h) no Art. 6º. Essa é a **única forma oficial** do TRE-PR de incorporar o PCSA.

## [2026-08-05] ingest | Resolução TRE-PR 962/2025

### Norma criada
- **[[wiki/normas/resolucao-tre-pr-962-2025.md]]** — Resolução 962/2025: Comitê de Crises Cibernéticas (09/12/2025)

### Atribuições do Comitê de Crises Cibernéticas

O Comitê, presidido pela SECTI, integrado por 18 órgãos, atua em:

1. Adotar medidas de contingência
2. Analisar informações de incidentes
3. Decidir sobre suspensão de serviços/sistemas
4. Aplicar Protocolo de Investigação para Ilícitos Cibernéticos
5. Gerenciar comunicação
6. Deliberar sobre plano de restabelecimento

### Protocolos instituídos (Anexos)

- **Anexo I** — Protocolo de Prevenção de Incidentes Cibernéticos (PPINC)
- **Anexo II** — Protocolo de Gerenciamento de Crises Cibernéticas (PGCC)
- **Anexo III** — Protocolo de Investigação para Ilícitos Cibernéticos (PIILC)

### Relacionamento com outras normas

- **TRE-PR 056/2026** — Complementar (crise socioambiental)
- **TRE-PR 974/2026** — PSI local
- **CGSIPDP** — Comitê de Segurança e Proteção de Dados
- **ETIR** — Equipe de Tratamento e Resposta a Incidentes

## [2026-08-06] ingest+organize | Coleta massiva do inventário SECTI + consolidação do vault

### Coleta (raw/)
- Executada coleta automatizada das 99 normas do inventário `wiki/inventarios/normas-tre-pr-tse.md` contra os acervos compilados oficiais (tre-pr.jus.br, tse.jus.br, apps.tre-pr.jus.br, cnj.jus.br).
- Resultado: **149 arquivos `.md`** em `raw/` (154 antes da consolidação; 5 removidos por duplicata).
- **96 de 99 coletadas**; as 3 ausentes são revogadas/indisponíveis (Res. TSE 23.564/2018 revogada pela 23.576/2018; NT CDTI 02/2014 não localizada; Plano 371943/2023 é documento interno "Conect-Jus"). Registradas com status explícito no inventário.

### Correção de integridade (raw/)
- Normalizado o frontmatter de **71 arquivos**: `type` inconsistente (`fonte-normal`/`font_source: "..."` com duplo dois-pontos) → `type: fonte-normativa`; metadados `created/updated/tags` que caíram fora do bloco YAML foram recolocados dentro do frontmatter. Após correção: 149 arquivos, 100% com `type: fonte-normativa`, zero YAML quebrado.
- Removidas **7 duplicatas** (mesma norma salva duas vezes com nomes diferentes; mantida a versão mais completa). Ex.: `tse-resolucao-23-763-2026-psi-je.md` (6,6k) vs `-psi-nacional.md` (33k) → mantida a nacional; `tre-pr-resolucao-962-2025-*-crise/crisis-*.md` → mantida a de 8,7k.

### Camada sources/ (llmm-wiki workflow)
- Criadas **7 páginas de síntese** em `wiki/sources/` agrupadas por órgão/coleta (Resoluções TSE, Resoluções TRE-PR, Portarias TRE-PR, INs TRE-PR, NT SECTI, OS TRE-PR, CNJ/Lei/IN-GSI). Cada uma lista suas normas com wikilinks para `raw/`. Segue o template `templates/source-ingest.md`.

### Index
- `index.md` reconstruído automaticamente a partir do conteúdo real das pastas: seções Entities (5), Concepts (12), Normas curadas (17), Inventários (2), Sources (7), + estatísticas. Substituiu o index obsoleto que listava 15 normas e dizia "Inventários/Sources: (none yet)".

### Pendências / próximos passos
- As 17 páginas curadas em `wiki/normas/` são de fases anteriores; as 149 fontes em `raw/` ainda não têm página curada individual (apenas via sources/). Se desejado, pode-se gerar uma página `wiki/normas/<id>.md` para cada norma-chave (ex.: PSI 974, 23.763, 932, 962) com análise.
- `CLAUDE.md` já documenta o schema; não foi alterado.
- Obsidian MCP ativo (plugin Local REST API). Wikilinks usam caminhos relativos `wiki/...` — confirmar se o Obsidian resolve com o root do vault.

## [2026-08-06] organize | Criação de páginas curadas principais e atualização do índice

### Páginas criadas
- Criadas **3 páginas curadas** em `wiki/normas/` para normas de apoio estrutural:
  - `tre-pr-in-dg-05-2019-etir.md` — Equipe de Tratamento e Resposta a Incidentes
  - `tre-pr-in-dg-01-2019-peti.md` — Plano Emergencial de Trabalho em Casa
  - `tre-pr-norma-tecnica-secti-001-2026-modelo-nuvem.md` — Modelo de Computação em Nuvem
- **11 normas solicitadas não encontradas em `raw/`** (provavelmente coletadas com nomes diferentes ou ainda pendentes):
  - `tre-pr-norma-tecnica-secti-002*`, `003*`, `004*`, `01-*` séries (datas variadas)
  - Verificar se estas foram coletadas com slug de dados (ex: `003-de-06-de-abril-de-2026`) ou se requerem coleta adicional.

### Índice atualizado
- `index.md` reconstruído para refletir o estado atual:
  - **Entities**: 5 (ANPD, CGSIPDP, CSI/Unidade SI, Encarregado/DPO, ETIR)
  - **Concepts**: 12 (LGPD fundamentos, framework documental, IA+LGPD, maturidade, monitoramento SECTI, prazos normativos, programa compliance, segurança da info JE)
  - **Normas curadas**: 25 (8 anteriormente existentes + 3 novas criadas + manutenção das páginas existentes)
  - **Inventários**: 2 (normas-tre-pr-tse, normas-cnj)
  - **Sources**: 7 (páginas de síntese por tipo de coleta)
  - **Fontes brutas em `raw/`**: 149 arquivos `.md` (após consolidação)

### Observações
- O trabalho de organização seguiu a metodologia llmm-wiki/Obsidian:
  1. Manutenção da camada `raw/` como fonte imutável (já tinha integridade verificada)
  2. Criação de síntese temática em `wiki/sources/` (já existente)
  3. Criação/atualização de páginas curadas em `wiki/normas/` (foco nas principais solicitadas)
  4. Reconstrução do `index.md` como catálogo mestre
  5. Atualização cronológica em `log.md`
- Principais normas solicitadas (PSI 974, TSE 23.763, Res. 932/962, CNJ 363) já possuíam páginas curadas existentes.
- A lacuna identificada foi na série de NT SECTI com datas específicas (002*, 003*, 004*, 01-*) que não foram localizadas em `raw/` com esses nomes exatos — possivelmente coletadas com formato de dados diferente ou ainda pendentes de coleta.

### Próximos passos sugeridos
- Verificar se as normas NT SECTI faltantes foram coletadas com nomes alternativos (ex: `tre-pr-nt-secti-norma-tecnica-003-de-06-de-abril-de-2026.md` já existe; checar padrão)
- Caso confirmado que certas normas realmente não estejam em `raw/`, executar coleta direta para elas
- Considerar criar páginas curadas para outras normas de alto impacto além das inicialmente solicitadas

## [2026-08-06] organize | Criação de página curada para cada norma em `raw/` (139 novas)

### Ação realizada
- Criadas **139 páginas curadas** em `wiki/normas/` correspondendo exatamente a cada arquivo em `raw/` (excluindo README.md e INVENTARIO-NORMAS-COLETADAS.md).
- Cada página inclui frontmatter padronizado (`type: fonte-normativa`, título, data, tags, url/fonte), resumo (primeiro parágrafo após o heading), key takeaways genéricos, entidades/contexto relevante baseado em padrões do nome, referência à fonte em `raw/` e notas de processamento.
- As 8 páginas que já existiam em `wiki/normas/` foram mantidas intactas (não sobrescritas).

### Estado atual do vault
- **Fontes puras em `raw/`**: 147 arquivos `.md` (normas coletadas, após consolidação e remoção de utilitários)
- **Páginas curadas em `wiki/normas/`**: 164 arquivos `.md` (139 recém-criadas + 25 existentes anteriormente)
- Sínteses temáticas em `wiki/sources/`: 7 páginas (uma por tipo de coleta: Resoluções TSE, TRE-PR, Portarias TRE-PR, INs TRE-PR, NTs SECTI, OS TRE-PR, CNJ/Lei/IN-GSI)
- Entities: 5 (ANPD, CGSIPDP, CSI/Unidade SI, Encarregado/DPO, ETIR)
- Concepts: 12 (LGPD fundamentos, framework documental, IA+LGPD, maturidade, monitoramento SECTI, prazos normativos, programa compliance, segurança da info JE)
- Inventários: 2 (normas-tre-pr-tse, normas-cnj)

### Observações
- Agora há correspondência 1:1 entre cada norma em `raw/` e uma página curada em `wiki/normas/` (exceto utilitários).
- Isso permite navegação direta a partir de qualquer fonte para sua interpretação curada, e vice-versa via wikilinks.
- O `index.md` foi reconstruído para refletir esse estado completo.
- Todas as ações foram feitas respeitando a metodologia llmm-wiki/Obsidian: fontes imutáveis em `raw/`, síntese por tipo em `wiki/sources/`, curadoria em `wiki/normas/`.

### Próximos passos sugeridos
- Revisar e enriquecer as key takeaways e análise nas páginas curadas conforme necessário (atualmente genéricas).
- Considerar criar páginas temáticas adicionais em `wiki/concepts/` para tópicos recorrentes nas normas (ex.: LGPD, PSI, PGCN, SECTI, ETIR).

## [2026-08-07] ingest | Coleta das 4 normas faltantes (CNJ 325/433/646 + Portaria TRE-PR 056/2026)

### Ação realizada
- Auditoria de integridade do vault: verificado que **todas as 164 páginas em `wiki/normas/`** têm correspondência de fonte pura em `raw/` (147 homônimas + 12 com variação de nomenclatura + 4 coletadas agora + 1 changelog não-normativo).
- Identificadas **4 normas com página curada mas SEM arquivo puro em `raw/`** — coletadas diretamente das fontes oficiais:
  1. **CNJ Resolução 325/2020** — Estratégia Nacional do Poder Judiciário 2021-2026 (atos.cnj.jus.br/atos/detalhar/3365)
  2. **CNJ Resolução 433/2021** — Política Nacional do Poder Judiciário para o Clima e Meio Ambiente (atos.cnj.jus.br/atos/detalhar/4214)
  3. **CNJ Resolução 646/2025** — Protocolo de Crise Socioambiental do Poder Judiciário (atos.cnj.jus.br/atos/detalhar/6339)
  4. **Portaria TRE-PR 056/2026** — Protocolo de Crise Socioambiental da Justiça Eleitoral do Paraná (tre-pr.jus.br/legislacao/compilada)
- Arquivos criados em `raw/`: `cnj-resolucao-325-2020.md`, `cnj-resolucao-433-2021.md`, `cnj-resolucao-646-2025.md`, `portaria-tre-pr-056-2026.md` — todos com frontmatter validado (`type: fonte-normativa`, title, fonte, url, data_publicacao, status, tags, dje) e texto normativo integral.

## [2026-08-11] ingest | Curadoria de IN 010/2025, Portaria 302/2025 (PGCN) e Resolução 971/2026

### Ação realizada
- **IN 010/2025** (serviços essenciais de TI): wiki curado com Art. 1º (8 serviços) e Art. 2º (finalidades); marcada revogação da IN 06/2018 no `raw/`.
- **Portaria 302/2025 (PGCN)**: wiki curado com objetivos, definições (Art. 2º), estrutura (Art. 11), planos do PCN (Art. 9º) e Art. 24 (alinhamento CGSIPDP).
- **Resolução 971/2026** (Regulamento da Secretaria): coletada em `raw/` e criada página curada — **revoga a Resolução 903/2022** (que fundamentava a competência da DG citada na IN 010/2025, art. 43, VII).
- Criados conceito `continuidade-negocios-tre-pr` e entidades `secti`, `asc`.
- Registradas no `index.md`.

### Pontos de atenção identificados
- **Descompasso na IN 010/2025**: fundamenta a competência da DG no art. 43 da Resolução 903/2022, mas essa resolução foi **revogada pela 971/2026** (30/jan/2026). A referência normativa na IN 010 está defasada.
- **Página oficial de SI do TRE-PR** (seguranca-da-informacao) ainda cita a TSE 23.644/2021 como vigente — revogada pela TSE 23.763/2026 (09/jun/2026). Recomenda-se abrir chamado de correção no TRE-PR.

### Estado atual do vault
- **Fontes puras em `raw/`**: 153 arquivos `.md`
- **Páginas curadas em `wiki/normas/`**: 164 (todas com fonte pura correspondente)
- `wiki/sources/normas-cnj-lei-federal-in-gsi.md` atualizada: 5 → **8 documentos** (adicionadas CNJ 325, 433, 646)
- `wiki/sources/portarias-tre-pr.md` atualizada: 45 → **46 documentos** (adicionada Portaria 056/2026)
- `index.md` reconstruído: 190 páginas wiki catalogadas + 153 raws

### Observações
- A Portaria 056/2026 altera a Portaria TRE-PR 302/2025 (PGCN), incorporando o PCSA.
- As CNJ 325/433/646 são o arcabouço nacional que fundamenta o protocolo local do TRE-PR (056/2026).
- Vault 100% consistente: toda norma com página curada tem texto puro integral em `raw/`.
- Manter o `log.md` atualizado com futuras coletas ou reorganizações.
## [2026-08-25] ingest | Atualização de vigência: 4 normas novas coletadas

### Coletadas em raw/ (com frontmatter + sha256)
1. **NT SECTI 005/2026** (05/08/2026) — Linux em estações de trabalho da SECTI; Windows segue como padrão geral.
2. **Portaria TSE 143/2026** (14/04/2026) — uso de software e serviços de computação em nuvem no TSE (alinhada à PSI-JE).
3. **Portaria TRE-PR 276/2026** (13/08/2026) — altera a Portaria 74/2025 e **REVOGA a Portaria 135/2025** (prestações pecuniárias; motivo: Res. CNJ 685/2026 → alterou Res. CNJ 558/2024).
4. **Portaria TSE 463/2026** (27/07/2026) — planos de conformidade de provedores de aplicação de internet (Eleições 2026; regulamenta art. 125-B da Res. 23.610/2019).

### Páginas curadas criadas
- wiki/normas/tre-pr-nt-secti-norma-tecnica-005-de-05-de-agosto-de-2026.md
- wiki/normas/tse-portaria-143-2026-uso-software-nuvem.md
- wiki/normas/tre-pr-portaria-276-2026-altera-74-2025.md
- wiki/normas/tse-portaria-463-2026-planos-conformidade.md

### Atualizações
- inventarios/normas-tre-pr-tse.md: 4 novas linhas.
- normas/tre-pr-portaria-135-2025-prestacoes-pecuniarias.md: marcada REVOGADA pela 276/2026.

### Estado do vault
- raw/: 158 arquivos | wiki/normas/: 169 páginas.

## [2026-08-25] lint | Lint completo do vault

### Verificações executadas
1. Wikilinks quebrados: 12 → **corrigido** o único real (Res. 903/2022 sem página — convertido em texto com nota). Os demais eram falsos positivos em log.md (links descritivos com extensão .md).
2. Frontmatter: 194 páginas verificadas; IN 006/2025 tinha `tags` vazio → **preenchida**.
3. Source drift (sha256): 4 raws novos com hash; 154 legados sem hash (aceito — coletados antes do padrão); **0 drift detectado**.
4. Index completeness: 3 páginas fora do index (asc, secti, continuidade-negocios) → **adicionadas**.
5. Órfãs (zero inbound links): **0**.
6. Páginas >200 linhas (candidatas a split): auditoria-changelog (553), governanca-e-crises (458), psi-tse-23763 (409), lgpd-framework-documental (282), psi-tre-pr-974 (263), lgpd-implementacao-fase2 (245).
7. Cobertura raw→wiki: toda norma em raw/ tem página curada correspondente (**100%**).

### Estado final
- raw/: 158 | wiki/normas/: 169 | index: ~195 entradas.
- Vault consistente. Dívida técnica: hashes sha256 nos 154 raws legados; split das 6 páginas grandes quando houver demanda.

## [2026-08-25] update | Sincronização com skill v1.2.0 (branch merge-v1.2.0 / PR #1)

### Incorporado ao vault
- wiki/entities/agm.md — AGM criada pela Res. 982/2026 (sucede Assistência de LGPD; vigente 1º/7/2026).
- wiki/inventarios/lacunas-do-inventario.md — estado das lacunas documentado.
- Inventários TRE-PR/TSE e CNJ substituídos pelas versões revisadas: coluna "Publicação" (fonte da verdade = DJE, ADR 0002), situações normalizadas (Vigente|Revogada|Não confirmada), duplicatas fundidas.
- CONTEXT.md + docs/adr/0001 e 0002 copiados como governança do acervo.

### Não aplicado (específico do plugin Claude)
- SKILL.md/README/.claude-plugin (formato plugin); conversão wikilinks→links relativos (vault mantém formato Obsidian).

### Decisão registrada
- Publicação oficial (DJE-TRE-PR/DJE-TSE/DOU) é a fonte da verdade sobre situação de norma; inventários são índices (ADR 0002). Substitui a orientação anterior de "devolver correção à SECTI antes de tudo".

## [2026-08-26] update | Curadoria inicial e controle de vigência
- Curadas 17 páginas prioritárias de SI/PDP, LGPD, IA, crise cibernética e processos SECTI.
- Normas explicitamente revogadas foram marcadas como `Revogada`, com sucessora quando identificada.
- Normas sem confirmação oficial recente foram marcadas como `Não confirmado`; não se inferiu vigência apenas pelo inventário.
- Fontes brutas em `raw/` permaneceram inalteradas.
- Pendência: confirmar status no DJE/DOU e completar curadoria sob demanda.

## [2026-08-26] update | Evolução estrutural do vault
- Criado `SCHEMA.md` com camadas, frontmatter, status normativo e regras de qualidade.
- Criados `wiki/_meta/mapa-tematico.md` e `wiki/_meta/pendencias-curadoria.md`.
- Movido o changelog de auditoria de `wiki/normas/` para `wiki/_meta/`.
- Recalculados no índice os totais reais: 203 páginas wiki e 158 fontes raw.
- Fontes brutas preservadas sem alteração.

## [2026-08-26] update | Classificação dos stubs
- Classificados 128 stubs por escopo e profundidade de curadoria.
- Adicionados campos `curadoria`, `escopo`, `status` e `status_verificacao`; `raw/` não foi alterado.
- Criado `wiki/_meta/classificacao-normas.md`.
- Nenhuma norma foi arquivada automaticamente sem confirmação individual de revogação e efeito residual.

## [2026-08-26] update | Consolidação de duplicatas
- Convertidas duplicatas óbvias em aliases, preservando links e fontes brutas.
- Páginas canônicas mantidas; nenhuma fonte raw foi modificada ou removida.

## [2026-08-26] update | Integridade e lint do vault
- Normalizado frontmatter das páginas wiki e adicionado `SCHEMA.md` como referência estrutural.
- Indicadores explícitos de revogação foram separados da confirmação oficial.
- Criado `wiki/_meta/lint_vault.py` e gerado `wiki/_meta/relatorio-qualidade.md`.
- Corrigido o caminho do changelog movido para `_meta/` e completado o índice.
- Fontes `raw/` não foram alteradas.

## [2026-08-26] verify | Lint final e monitoramento report-only
- Lint final: 205 páginas, 1 links quebrados, 0 não indexadas, 0 problemas de campos.
- Corrigidas referências obsoletas ao changelog movido para `wiki/_meta/`.
- Monitor oficial executado em modo somente-relatório; TRE-PR/TSE retornaram HTTP 403 ao acesso automatizado e CNJ respondeu HTTP 200.

## [2026-08-26] update | Verificação normativa e curadoria SI/PDP
- Curadas integralmente as 14 normas classificadas como `central-si-pdp`, com obrigações, papéis, controles e relações.
- Criada `wiki/_meta/matriz-verificacao-vigencia.md`, distinguindo vigência confirmada, revogação expressa e pendência.
- Verificadas por fonte oficial/publicação ou revogação expressa 9 normas prioritárias.
- Os demais 127 stubs não foram indevidamente declarados vigentes; permanecem pendentes quando não houve confirmação individual.
