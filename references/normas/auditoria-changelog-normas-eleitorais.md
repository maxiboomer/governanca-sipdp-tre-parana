---
title: Auditoria — Changelog da análise de normas eleitorais
type: normas-changelog
created: 2026-07-27
updated: 2026-07-27
tags: [auditoria, changelog, normas-eleitorais]
---

# Changelog — skill analise-normas-eleitorais

Atualização consolidada em 23/6/2026. Resumo das mudanças em relação à versão anterior.

## Como aplicar este kit
1. Substitua a pasta da skill pela versão deste kit, mantendo a estrutura:
   - `SKILL.md` na raiz
   - `references/` com os 4 arquivos `.md`
2. O `CHANGELOG.md` é informativo; não precisa ir para a instalação da skill (mas não atrapalha).
3. Estrutura esperada:
   ```
   analise-normas-eleitorais/
   ├── SKILL.md
   └── references/
       ├── estrutura-normativa-psi.md
       ├── governanca-ciberseguranca-tre-pr.md
       ├── prazos.md
       └── psi-tre-pr-974.md
   ```

## 1. PSI nacional: troca de norma (revogação)
- **Res. TSE 23.763/2026** substitui a **Res. TSE 23.644/2021** (revogada — art. 36).
- Reescrito [[normas/psi-tse-23763-2026]] para a norma nova.
- Principais mudanças de conteúdo (não só numeração):
  - Princípios: saiu "DICA+AI"; agora D-I-C-A + **Não repúdio** (art. 3º).
  - Nova **Unidade de SI desvinculada da TIC** (art. 17, II; 21).
  - **16 temas táticos obrigatórios** (art. 9º), incluindo IA, nuvem, trabalho remoto.
  - Criptografia: regra **com exceção justificada** (art. 24, §3º).
  - Revisão: **máx. 4 anos, ano não eleitoral** (art. 19, I).
  - Adaptação dos tribunais: **31/12/2027** (art. 30).
  - ISO 27001:2022 / 27002:2022 / 27005:2023.

## 2. PSI local do Paraná
- **Novo:** [[normas/psi-tre-pr-974-2026]] (Res. TRE-PR 974/2026).
- Registrado o **descompasso temporal**: a 974/2026 (15/4/2026) ancora-se na revogada
  23.644/2021 e é anterior à PSI nacional nova; precisa de revisão de alinhamento.
- Registrada a **divergência de princípios**: a 974 mantém irretratabilidade e
  auditabilidade (rol antigo); prevalece a nacional (TSE > TRE).
- Mapa de divergências local × nacional incluído.

## 3. Governança e crises cibernéticas (TRE-PR)
- **Novo:** [[normas/governanca-e-crises-tre-pr]], cobrindo:
  - **Res. TRE-PR 932/2024** — Sistema de Governança (cria o CGSIPDP); já alterada pela
    **Res. 980/2026** (CGER → CGERI).
  - **Res. TRE-PR 962/2025** — Comitê de Crises Cibernéticas + protocolos PPINC/PGCC/PIILC
    (documentada na íntegra a partir do texto oficial).
- Pontos de atenção registrados:
  - Dupla função na 962: **preside** (titular da Secretaria de TI) vs. **coordena quando
    acionado** (titular da Coordenadoria de Segurança, IA e Governança de TI).
  - **CGTIC = CGTI** (variação de redação herdada do protocolo-modelo do CNJ).

## 4. Ajustes transversais no SKILL.md
- Frontmatter (description) atualizado para disparar com as novas normas e siglas
  (CGSIPDP, Comitê de Crises Cibernéticas, Sistema de Governança do TRE-PR).
- Tabela de normas no escopo, tabela de temas-chave, regras de interpretação,
  princípios e referências complementares atualizadas.
- [[concepts/prazos-normativos-tre-pr]] atualizado (PSI nacional, PSI local, crises).

## Pendências sinalizadas (não implementadas — fora do escopo pedido)
- **Res. TRE-PR 959/2025** (IA) — citada como correlata, não detalhada.
- Norma Técnica 01/2026 SECTI (nuvem) e INs da SECTI — listadas como pistas.
- Conferência final contra os textos "compilados" oficiais antes de uso em parecer.
- Verificação de vigência/atualidade da 855/2020 e da 23.650/2021 (informadas como
  vigentes pelo usuário; não auditadas).

---

# Atualização de 22/7/2026

Auditoria da skill contra o texto oficial compilado da Res. TSE 23.763/2026 no portal
do TSE. **Todas as afirmações sobre a nova PSI foram confirmadas** (revogação da
23.644 pelo art. 36, prazo de 31/12/2027 do art. 30, princípios do art. 3º, 16 temas
do art. 9º, Unidade de SI desvinculada da TIC do art. 21, reuniões trimestrais,
revisão quadrienal em ano não eleitoral, criptografia com exceção justificada,
comunicação de incidentes do art. 23). Nenhuma menção residual tratava a 23.644/2021
como vigente. Correções aplicadas:

## 1. Dependências abertas do nível estratégico (NOVO)
- **Estratégia Nacional de Cibersegurança da JE: não publicada.** A anterior (Portaria
  TSE 590/2022) cobria 2021–2024 e está vencida; a nova está em formulação por GT da
  **Portaria TSE 294, de 3/6/2026** (DJE-TSE nº 92, de 9/6/2026; composição alterada
  pela Portaria 350/2026). Registrado no SKILL.md e em [[normas/psi-tse-23763-2026]],
  com a lista de dispositivos da 23.763 que dependem dela.
- **Norma de termos e definições (art. 2º): não reeditada.** Continua valendo a
  **Portaria TSE 444/2021**, não revogada pela 23.763. Registrada com ressalva de
  fragilidade (norma de âmbito interno do TSE, ancorada na Res. 23.501/2016).

## 2. Inventário tático nacional (NOVO)
- Tabela dos 16 temas do art. 9º, II × normativos do TSE existentes (Portarias 454,
  455, 457, 458, 459, 460 e 540/2021, e 262/2024), com marcação das lacunas.
- Registrado que o art. 9º, §6º apenas **faculta** ao TSE editar modelos — a ausência
  de norma nacional não suspende o dever local de editar os normativos táticos.
- Sinalizada a cobertura parcial local: NT 01/2026 SECTI (nuvem) e Res. TRE-PR
  959/2025 (IA), a verificar se atendem o nível tático exigido.

## 3. Correção de erro no organograma
- O diagrama anterior subordinava a Unidade de SI à CSI. **Errado:** o art. 21, caput
  a subordina diretamente à alta administração; a CSI é colegiado, não chefia.
  Corrigido no SKILL.md e em [[normas/psi-tse-23763-2026]], com nota de advertência —
  o desenho institucional é o ponto em disputa na adaptação do TRE-PR.

## 4. Art. 4º (monitoramento de recursos de TIC) — antes ausente
- Nova seção em [[normas/psi-tse-23763-2026]] e 3 linhas na tabela de temas-chave.
- Interface explícita com a PGPPDP (art. 4º, §2º, III) e com a tabela de temporalidade
  (§2º, II). Gancho normativo para exigir base legal e RIPD em monitoramento sistemático.

## Verificado e SEM alteração
- Res. TSE 23.763/2026: sem alterações posteriores.
- TRE-PR: nenhuma norma nova de SI desde a 974/2026. A página oficial de Segurança da
  Informação segue listando 974/2026, 962/2025, 959/2025 e NT 01/2026 SECTI.

## Pendências que permanecem
- Res. TRE-PR 959/2025 (IA) ainda não detalhada em referência própria.
- Vigência da Res. TRE-PR 855/2020 e da Res. TSE 23.650/2021 não auditada contra texto
  compilado (só a 23.763 foi conferida nesta rodada).
- Afirmação "a 23.644/2021 exigia 11 temas táticos (a–k)" não reconferida contra o
  texto revogado — tratar como plausível, não verificado.
- Acompanhar a publicação da nova Estratégia Nacional: quando sair, revisar o SKILL.md
  e reavaliar o cronograma de revisão da PSI local do Paraná.

## 5. Auditoria contra a norma revogada (23.644/2021) — rodada complementar
Texto compilado da 23.644/2021 conferido no portal do TSE.

**Confirmado:**
- 11 temas táticos (a–k) no art. 9º, II ✔
- Princípios com irretratabilidade e auditabilidade no art. 3º ✔
- Menção à IN nº 01 GSI/PR/2008 no art. 9º, §2º ✔
- Revisão a cada 3 anos (art. 12, I) e adaptação até 31/12/2021 (art. 24) — [[concepts/prazos-normativos-tre-pr]]
  já estava correto, sem alteração ✔

**CORRIGIDO — erro de conteúdo:** a skill afirmava que a 23.644/2021 tratava criptografia
como obrigação direta e que a exceção justificada seria novidade da 23.763/2026. **Falso.**
O art. 17, parágrafo único da 23.644 já previa a exceção, em redação quase idêntica ao
atual art. 24, §3º. A mudança real é de alcance: a norma antiga impunha criptografia a
toda informação classificada em qualquer grau de sigilo (art. 17, caput); a nova a
insere num rol de salvaguardas (art. 24, §2º), sem o comando categórico. Reescrito em
[[normas/psi-tse-23763-2026]], com a implicação prática para parecer.

**Contexto acrescentado:** os 5 temas táticos novos derivam do art. 22 da própria
23.644/2021, que mandava a revisão seguinte considerar nuvem, trabalho remoto e novas
soluções de TIC — útil para demonstrar continuidade normativa.

## 6. PGPPDP (Res. TSE 23.650/2021) — status
Nenhum indício de revogação ou alteração. Citada como vigente pela Res. TSE 23.760/2026
(março/2026) e pelo Calendário Eleitoral do TSE atualizado em julho/2026, além da página
institucional de Proteção de Dados do TSE (prazos do art. 14). **Ressalva: verificação
por indícios, não auditoria artigo a artigo.**

## Pendências remanescentes após esta rodada
- Res. TRE-PR 855/2020 (LAI local): vigência não verificada.
- Res. TRE-PR 959/2025 (IA): sem referência própria.
- Portaria TSE 444/2021: conteúdo das definições não incorporado à skill (só a remissão).
- Acompanhar publicação da nova Estratégia Nacional de Cibersegurança (GT da Portaria
  TSE 294/2026) — quando sair, revisar nível estratégico e cronograma da PSI local.

## 7. Portaria TSE 444/2021 incorporada (NOVO ARQUIVO)
[[normas/psi-termos-portaria-tse-444-2021]] — glossário da PSI conferido contra o texto
oficial compilado do TSE em 22/7/2026 (DJE-TSE nº 131, de 12/7/2021). **57 definições**
(art. 2º, incisos I a LVII), organizadas por bloco temático, com o inciso preservado
para citação.

**Achado que altera análise já registrada na skill:** o inciso XXXIV define
"**Irretratabilidade (ou não repúdio)**" como um só conceito. Logo, a substituição
operada pela 23.763/2026 é **renomeação, não supressão**, e a divergência com a
Res. TRE-PR 974/2026 quanto a esse princípio é **nominal**. A divergência real é a
**auditabilidade** — não recepcionada pela PSI nova e sequer definida no glossário.
Corrigidos os trechos correspondentes no SKILL.md (seção de princípios e alerta do art. 2º).

**Segundo achado:** o inciso L (conceito de "segurança da informação") ainda se orienta
pelo rol antigo, incluindo irretratabilidade — descompasso de redação com o art. 3º
da PSI vigente.

**Terceiro achado:** o art. 4º da Portaria 444 exige revisão em no máximo 3 anos.
Publicada em 12/7/2021, a revisão está **vencida desde julho/2024** (~2 anos).
Registrado em [[concepts/prazos-normativos-tre-pr]] (tabela da PSI nacional).

**Quarto achado — descompasso de ciclo de vida:** o inciso XII descreve 6 fases; o
art. 24 da Res. 23.763/2026 lista 11. Prevalece o art. 24 (norma superior e posterior).

**Lacunas mapeadas:** o glossário não define auditabilidade, vocabulário LGPD/PGPPDP
(dado pessoal, titular, encarregado), nuvem, IA, trabalho remoto, provedor de serviços,
inteligência cibernética, segurança cibernética, nem as estruturas do Cap. X (CSI,
Unidade de SI, GSI, ETIR). Os 5 temas táticos novos estão sem vocabulário oficial.

**Interface com continuidade de negócios:** incisos IV, V e XVII trazem definições de
atividades críticas, atividades precípuas e continuidade de negócios — vocabulário de
2016, mais estreito que a ISO 22301; ressalva registrada no arquivo.

Integrado ao SKILL.md: frontmatter, lista de referências, 4 linhas na tabela de
temas-chave e fórmula de citação segura no arquivo de referência.

**Pendências remanescentes:** Res. TRE-PR 855/2020 (vigência), Res. TRE-PR 959/2025
(sem referência própria), [[normas/psi-tre-pr-974-2026]] e [[normas/governanca-e-crises-tre-pr]]
ainda não auditados contra texto oficial, eixo LAI sem verificação, e marcador de
procedência por norma não implementado.

## 8. PGPPDP (Res. TSE 23.650/2021) auditada — NOVO ARQUIVO
[[normas/pgppdp-tse-23650-2021]]. Texto integral conferido em 22/7/2026 (fornecido pelo
usuário a partir do compilado oficial do TSE). 30 artigos. **Sem revogação ou alteração.**
A cobertura anterior — um diagrama e 6 linhas de tabela — estava tecnicamente correta
onde afirmava algo, mas **incompleta em pontos que invertem conclusão**:

**CORRIGIDO 1 — matriz de papéis.** A skill dizia apenas "Controlador: TSE e TREs".
O art. 18 tem 4 figuras e 3 parágrafos decisivos: **§2º — o Tribunal atua como OPERADOR
quando trata em nome do Tribunal controlador**; **§1º — o Juízo Eleitoral não se equipara
a controlador**; §3º — finalidades diversas sobre o mesmo dado = controladores isolados,
não conjuntos. Consequência: papel deve ser definido **por tratamento**, não por
instituição. Corrigido no diagrama do SKILL.md + nova regra de interpretação 4-A.

**CORRIGIDO 2 — Encarregado.** A skill escrevia "Encarregado / DPO". O art. 18, III define
Encarregado como **unidade** indicada pelo Tribunal (diverge da LGPD art. 5º, VIII, que
fala em pessoa); o art. 19, §2º fala em "representante do Encarregado".

**ACHADO 3 — remissão morta.** O art. 10, I remete à **Res. TSE 23.644/2021** (revogada),
assim como a nota do art. 27. São agora **duas** normas ancoradas na PSI revogada:
esta (nacional) e a Res. TRE-PR 974/2026 (local).

**ACHADO 4 — revisão vencida.** Art. 22: máx. 3 anos; publicada em set/2021 → vencida
desde set/2024. Terceira norma do conjunto em atraso (com a Portaria TSE 444/2021).

**ACHADO 5 — conflito de prazo de incidente.** PGPPDP art. 15, IV: 72 horas úteis.
PGPPDP art. 25: prevalece o prazo da ANPD. Res. CD/ANPD 15/2024, arts. 6º e 9º: 3 dias
úteis, "ressalvada legislação específica". **As duas se remetem mutuamente.** Orientação
registrada: adotar 3 dias úteis. Acrescentado o dever de registro do incidente por 5 anos
(Res. ANPD 15/2024, art. 10), ausente da PGPPDP. [[concepts/prazos-normativos-tre-pr]] atualizado.

**ACHADO 6 — "revisão bianual" do RIPD** (art. 15, §1º, II) é ambíguo: bienal (2 anos)
× bianual (2×/ano). Recomendado fixar o intervalo expressamente em norma local.

**QUESTÃO ESTRUTURAL TRE-PR:** a PGPPDP (art. 16) exige Encarregado + CGPD; a PSI nova
(art. 18) pressupõe CGPD e CSI como colegiados **distintos**. O TRE-PR opera com o
**CGSIPDP** fundido. Registrado como ponto que exige decisão expressa e fundamentada na
adaptação até 31/12/2027 — sem afirmar não conformidade.

**Conteúdo operacional incorporado, antes ausente:** art. 8º (9 obrigações de contratados
— checklist contratual), art. 12 (itens obrigatórios no portal), art. 13 (linguagem para
crianças e adolescentes), art. 7º (tarja/supressão em contratos publicados), art. 15, §3º
(temporalidade × dados constrangedores), art. 15, §1º, III (RIPD consolidado e enviado ao
CGPD do TSE), art. 17 (fluxo unidades → ETIR → Encarregado), art. 24 (interoperabilidade),
art. 3º p.ú. (âncora normativa da tensão LAI × LGPD).

**Divergência de gatilho registrada:** PGPPDP usa "risco ou dano relevante ao titular";
PSI nova (art. 23, I) usa incidente "crítico ou elevado" — critérios distintos na mesma
cadeia de comunicação.

**Confirmado sem alteração:** princípios (boa-fé + 10), bases legais (arts. 5º-6º),
direitos do titular (arts. 11-14), prazos de 15 e 20+10 dias, transferência internacional
(art. 9º), RoPA (art. 15, II), complementaridade (art. 27), casos omissos (art. 29).

**Pendências:** Res. TRE-PR 855/2020 e 959/2025; [[normas/psi-tre-pr-974-2026]] e
[[normas/governanca-e-crises-tre-pr]] ainda não auditados contra texto oficial; eixo LAI
sem verificação; marcador de procedência por norma não implementado.

## 9. Res. TRE-PR 974/2026 auditada contra o texto oficial (22/7/2026)
Texto integral conferido no portal do TRE-PR (DJE-TRE-PR nº 070, de 20/4/2026, p. 9-15).
18 artigos, 6 capítulos.

**RESULTADO: o arquivo [[normas/psi-tre-pr-974-2026]] estava CORRETO.** Conferidos e confirmados:
estrutura de capítulos, art. 2º (rol de princípios), art. 3º (destinatários), art. 7º
(CGSIPDP), art. 8º e §único (poder cautelar do GSI), art. 9º (ETIR), art. 5º §único
(vedação a pendrive/HD), art. 6º (deveres), arts. 10-12, art. 13 (continuidade),
arts. 14-18. **Nenhum erro de transcrição.** Carimbo de verificação inserido no arquivo.

**OMISSÃO CORRIGIDA — art. 4º:** a 974 **tem glossário próprio com 34 definições**
(incisos I a XXXIV), que o arquivo não registrava. Consequências:
- No âmbito da PSI local **não se depende da Portaria TSE 444/2021** — reduz a fragilidade
  antes apontada. A 444 passa a valer subsidiariamente, onde a 974 é silente.
- **Definições divergentes entre local e nacional:** *custodiante* (974, XII — por
  delegação do gestor da informação × 444, XIX) e *proprietário(a) da informação*
  (974, XXIV — quem produz × 444, XL — *proprietário do ativo*, instituído por cargo).
  São figuras distintas: atenção ao atribuir responsabilidade por classificação/inventário.
- Ciclo de vida (art. 4º, VII): 6 fases — diverge das 11 do art. 24 da PSI nacional.

**ACHADO — incoerência interna da 974:** o art. 2º eleva a **auditabilidade** a princípio
norteador, mas o **art. 4º, XXX** define "segurança da informação" sem ela, e o glossário
não a define em lugar nenhum. Como a irretratabilidade é sinônimo de não repúdio
(Portaria 444, XXXIV), **a auditabilidade é a única divergência real de princípios com a
PSI nacional — e é frágil no próprio texto local.** Se a revisão a retirar, não há perda
normativa real. Registrado nos princípios e no mapa de divergências.

**ACHADO — criptografia local mais rígida que a nacional.** Fecha a questão deixada em
aberto no item 5 deste changelog. O art. 12 da 974 impõe criptografia forte a informação
sigilosa **e a dado pessoal sensível**, em trânsito e em repouso, **sem cláusula de
exceção** — diferente da 23.644 revogada (art. 17, p.ú.) e da 23.763 vigente (art. 24,
§3º), ambas com exceção justificada. No TRE-PR, dispensar criptografia não tem base na
norma local. Atualizado também em [[normas/psi-tse-23763-2026]].

**ACHADO — o gatilho de revisão do art. 17 JÁ DISPAROU.** O dispositivo manda revisar
anualmente **ou** diante de alteração significativa "no arcabouço normativo nacional".
A Res. TSE 23.763/2026 é exatamente isso. O dever de revisar está ativo desde 15/6/2026,
independente do ciclo anual. Muda o enquadramento: a questão é *como sequenciar*, não
*se* revisar.

**Acrescentados à tabela de temas-chave:** art. 4º (definições), art. 12 (criptografia),
art. 13 (PGCN/PRD/PCO e testes periódicos), art. 15 (cláusulas contratuais após 20/4/2026),
art. 17 com o gatilho.

**Pendências:** [[normas/governanca-e-crises-tre-pr]] (Res. 932/2024 e 962/2025) e todo o
eixo LAI (Lei 12.527/2011 e Res. TRE-PR 855/2020) seguem sem auditoria. Res. TRE-PR
959/2025 sem referência própria. Marcador de procedência aplicado só na 974 — falta
estender aos demais arquivos.

## 10. Res. TRE-PR 932/2024 auditada contra o texto oficial (22/7/2026)
Texto compilado conferido (32 artigos, 10 capítulos), já com as alterações da Res. 980/2026.

**RESULTADO: [[normas/governanca-e-crises-tre-pr]] estava CORRETO** na parte da 932/2024.
Conferidos: revogação da Res. 876/2021 (art. 31), vigência (art. 32), renomeação CGER →
CGERI com incisos XVIII-XXI (Res. 980/2026), princípios (art. 1º), mecanismos e funções
(arts. 2º-3º), estrutura (art. 4º), Conselho (arts. 5º-6º), CGTI art. 10, VI, CGSIPDP
art. 14, reuniões (art. 21), transição (arts. 26-28) e os prazos de 28/02.
**Terceira auditoria consecutiva sem erro de transcrição.**

**🔴 ACHADO — CONFLITO DE PERIODICIDADE.** Art. 21, §2º: Comitês e Comissões realizam
**mín. 2 reuniões ordinárias anuais**, "salvo exigências específicas do **Conselho Nacional
de Justiça**". A Res. TSE 23.763/2026 (art. 21, §2º, XI) exige reuniões da CSI
**trimestrais obrigatórias**. A ressalva local menciona **apenas o CNJ** — não o TSE.
Se o CGSIPDP absorver funções de CSI, deverá 4 reuniões/ano sem acomodação textual.
Encaminhamento: incluir alteração do art. 21, §2º no pacote de adaptação.

**🔴 ACHADO — o gap estrutural não é o comitê.** Confronto entre o art. 14 da 932 (26
competências do CGSIPDP) e o art. 20 da PSI nacional (competências da CSI dos TREs):
o CGSIPDP **já exerce praticamente todo o rol**. Isso **corrige a análise do item 8** deste
changelog, que tratava o modelo fundido como o problema. O modelo é defensável. Faltam:
(1) a **Unidade de SI desvinculada da TIC** com o GSI como titular (art. 21 nacional) —
sem equivalente na 932 nem na 974; (2) o **escalonamento à CSI do TSE** (art. 20, XI).

**ACHADO — rito de adaptação mapeado (art. 6º, p.ú.):** criação, extinção e alteração de
atribuição ou finalidade de Comitês é deliberada pelo **Conselho de Governança** e
submetida à **Corte Regional Eleitoral**. Caminho a percorrer até 31/12/2027, com prazo
próprio das duas instâncias.

**ACHADO — inconsistência interna:** a Res. 980/2026 alterou o título da Seção III e o
art. 11, mas o **art. 4º, II, "3" ainda nomeia "CGER"**. A mesma unidade aparece com dois
nomes. Há ainda erro de redação no caput alterado do art. 11 ("Gestão **Estratégia**" em
vez de "Estratégica").

**⚠️ ACHADO — COGECONEG com base normativa remetida e não identificada.** A Comissão de
Gestão de Continuidade de Negócios consta do art. 4º, III, "2", mas o art. 17 diz que as
Comissões Permanentes são as instituídas por determinação do CNJ ou do TSE, com composição
e competência definidas pelo normativo do órgão superior. Os considerandos identificam a
norma superior de quase todas as comissões — **menos da COGECONEG** (e da COETIN).
A 932 remete a um normativo que ela própria não indica. Arcabouço substantivo tende a
estar na **PGCN da JE-PR** (Res. 974/2026, art. 13).

**Conteúdo incorporado, antes ausente:** arts. 19 e 20 (atribuições de presidente e de
secretário de colegiado, incluindo conteúdo mínimo da ata), art. 24 (publicidade de atas:
íntegra na intranet, extrato na internet, níveis diferenciados por deliberação), art. 25
(Relatório Anual da Governança), art. 8º (competências comuns aos Comitês, incl. inciso X
— definir no início do ano os riscos a mapear), art. 5º, §2º (Assessores CJ-3 equiparados
a Secretários no Conselho de Governança), art. 23, §2º (fluxo das deliberações à DG).
[[concepts/prazos-normativos-tre-pr]] ganhou bloco próprio da 932/2024.

**Pendências:** Res. TRE-PR 962/2025 (bloco de crises do mesmo arquivo) não auditada;
eixo LAI (Lei 12.527/2011 e Res. TRE-PR 855/2020) sem verificação; Res. 959/2025 sem
referência própria; marcador de procedência aplicado em 974 e 932 — falta nos demais.

## 11. Res. TRE-PR 962/2025 auditada contra o texto oficial (22/7/2026)
10 artigos + Anexos I (PPINC), II (PGCC) e III (PIILC). **Quarta auditoria consecutiva sem
erro de transcrição** — o arquivo estava correto, inclusive na distinção entre *presidir*
(titular da SECTI, art. 2º) e *coordenar quando acionado* (titular da Coordenadoria de
Segurança, IA e Governança de TI, art. 4º, §2º). Achados são de **omissão e de conflito
entre normas**, não de erro:

**🔴 1. Conflito de atribuição — comunicação ao CPTRIC-PJ.** Res. 932/2024, art. 14, VII
atribui ao **CGSIPDP** comunicar "sempre que for detectado incidente"; Res. 962/2025,
Anexo II, 3.9, I atribui à **Presidência** comunicar "quando constatada crise". Toda crise
é incidente — na crise as duas incidem, com atores diferentes e sem regra de harmonização.

**🔴 2. Comunicação à ANPD tratada como discricionária.** Anexo III, 2.2: o encarregado
comunica aos titulares "e, **se entender necessário**, à ANPD". Incompatível com LGPD
art. 48, PGPPDP art. 15, IV e Res. CD/ANPD 15/2024 (3 dias úteis; comunicação **pelo
controlador, por meio do encarregado** — art. 6º, §5º). Norma local não converte dever
vinculado em juízo de conveniência. Registrado também o erro de nomenclatura ("Agência"
em vez de **Autoridade** Nacional de Proteção de Dados) e a divergência com o Anexo II,
3.10, que menciona só a comunicação aos titulares.

**3. Três glossários simultâneos:** Portaria TSE 444/2021 (PSI nacional), art. 4º da
974/2026 (PSI local) e Anexo VIII da Portaria CNJ 162/2021 (crises, art. 7º da 962).
Termos como "incidente", "crise", "ativo" e "serviço essencial" podem divergir. Parecer
deve declarar qual glossário aplica.

**4. CGTIC × CGTI.** O Anexo II, 1.3 incumbe o "Comitê de Governança de TIC (CGTIC)" de
definir a **lista de serviços essenciais críticos**; a Res. 932/2024 institui o **CGTI —
Comitê de Gestão da TI**. A equivalência é interpretação, não texto. Verificação
prioritária levantada: **a lista existe?** Sem ela o PGCC opera sem objeto e o gatilho do
item 2.2, III fica sem referencial — além de ser insumo direto de BIA.

**5. Composição possivelmente desatualizada:** art. 1º, XIV arrola a "Assistência de LGPD
e Processos Institucionais". Conferir contra o organograma atual e a portaria de
designação.

**6. Destinatário divergente na comunicação ao TSE:** Anexo II, 3.7, XI manda comunicar à
**STI do TSE**; a Res. 23.763/2026, art. 23, I manda comunicar ao Encarregado e à **ETIR
do TSE**. Norma nacional é posterior e superior.

**7. Colisão de calendário:** art. 9º — protocolos revistos no 2º semestre de anos ímpares
→ próxima revisão em **2H2027**, mesmo semestre do prazo de adaptação à PSI nacional
(31/12/2027). Tratar como pacote único evita duas passagens pelo rito Conselho → Corte.

**8. Instrumentos de continuidade pressupostos:** Programa de Gestão de Continuidade de
Serviços de TIC (Anexo II, 2.1), plano de continuidade de serviços essenciais de TIC,
norma complementar de diretrizes de continuidade de TIC (Anexo II, 3.11, IV), planos de
contingência testados — somados à PGCN, PRD e PCO da Res. 974/2026, art. 13. Levantado
como inventário a confirmar (existência, vigência, data do último teste).

**Estado da auditoria:** verificadas contra texto oficial — Res. TSE 23.763/2026,
23.644/2021 (revogada), Portaria TSE 444/2021, Res. TSE 23.650/2021, Res. TRE-PR 974/2026,
932/2024 e 962/2025. **Pendente:** eixo LAI (Lei 12.527/2011 e Res. TRE-PR 855/2020) e
Res. TRE-PR 959/2025 (IA). Marcador de procedência aplicado em 974, 932 e 962.

## 12. Eixo LAI completo: Lei 12.527/2011 e Res. TRE-PR 855/2020 (22/7/2026)
Fecha a última pendência estrutural da skill. Dois arquivos novos:
[[normas/lai-12527-2011]] (lei federal) e [[normas/lai-tre-pr-855-2020]] (norma local).

### Lei 12.527/2011 — RESULTADO: todas as afirmações prévias da skill conferiam.
Achados de omissão (não de erro): art. 12 tem redação nova pela Lei 14.129/2021
(gratuidade virou regra, ressarcimento é exceção em §1º); arts. 8º-A e 8º-B incluídos
pela Lei 15.141/2025 (transparência de serviços sociais autônomos e conselhos de
fiscalização — sem aplicação direta ao TRE-PR); CGU e CMRI (arts. 16 e 35) são
instâncias do Executivo Federal e **não alcançam o Judiciário** — no TRE-PR, o art. 18
remete a "regulamentação própria", que é a Res. 855/2020; art. 19, §2º obriga informar
ao CNJ decisões que negarem acesso em grau de recurso; art. 4º é um quarto glossário do
ecossistema (junto com Portaria 444/2021, art. 4º da 974/2026 e Anexo VIII da Portaria
CNJ 162/2021).

### Res. TRE-PR 855/2020 — RESULTADO: o fluxo de prazos já registrado em [[concepts/prazos-normativos-tre-pr]]
estava CORRETO (D+2/D+10-15/D+20-15/+10). Achados:

**🔴 1. Competência de classificação (fecha pendência aberta em rodada anterior).**
Art. 24: ultrassecreto — só o Presidente; secreto — + Diretor-Geral e Assessor-Chefe da
Presidência; reservado — + Oficiais de Gabinete e Secretários. Rol nominal, mais
restrito que o critério federal (DAS 101.5). Vedada delegação nos dois primeiros graus.

**🔴 2. Cadeia recursal é escada de 5 destinatários** conforme quem decidiu (art. 18,
§2º) — não recurso hierárquico genérico. Segundo recurso ao Presidente (art. 19), salvo
se a decisão já foi dele. Recurso de reavaliação de classificação tem prazo de decisão
de **30 dias** (art. 26, §3º) — não confundir com os 10 dias do recurso comum.

**🔴 3. Art. 17 traz catálogo próprio de não-atendimento**, independente de
classificação formal: sigilo fiscal/bancário/telefônico/médico, avaliação de desempenho
e estágio probatório, procedimentos disciplinares e auditorias em andamento. É regime
distinto tanto da classificação (arts. 21-26) quanto do art. 27 (documentos
preparatórios/pessoais) — três regimes de restrição em paralelo na mesma norma.

**🔴 4. Referência morta ao art. 31, III** — cita a Res. 23.501/2016 (revogada duas
vezes) para regras de criptografia de sigiloso digital. Ler como remissão ao art. 24 da
Res. 23.763/2026 — mas, se o documento também for dado pessoal sensível, prevalece o
regime mais rígido do art. 12 da Res. 974/2026 (sem exceção).

**5. Nomenclatura órfã:** art. 41 atribui a definição do gestor da informação ao
"Comitê de Segurança do Tribunal", nome que não existe no Sistema de Governança vigente
— ler como CGSIPDP por sucessão funcional. Terceiro caso do mesmo padrão (após
CGTIC/CGTI e CGER/CGERI).

**6. Prazos transitórios vencidos** (arts. 40 e 42: reavaliação de documentos antigos e
apresentação do rol do TCI, ambos com prazo de jul/2022) — quarto item do ecossistema
com prazo transitório vencido e não fechado.

**Conteúdo operacional incorporado:** transparência ativa com 21 incisos, incluindo TLP
nominal semestral (art. 6º, XIV); canais e responsáveis por responder (arts. 12, 15);
sucessão de titular falecido (art. 28, §2º); rito de reconhecimento de acesso irrestrito
histórico com edital prévio de 30 dias (art. 29, §§7º-9º); regras físicas de expedição
de sigiloso (envelope duplo, gráficas credenciadas — arts. 31, 36); temporalidade com
1 ano extra pós-desclassificação (art. 34).

`SKILL.md` e [[concepts/prazos-normativos-tre-pr]] atualizados com as novas linhas de tema-chave e os prazos
recursais/de classificação que faltavam.

## Estado consolidado da auditoria (22/7/2026)
**Verificadas integralmente contra texto oficial:** Res. TSE 23.763/2026, Res. TSE
23.644/2021 (revogada), Portaria TSE 444/2021, Res. TSE 23.650/2021 (PGPPDP), Res.
TRE-PR 974/2026, Res. TRE-PR 932/2024, Res. TRE-PR 962/2025, Lei 12.527/2011, Res.
TRE-PR 855/2020. **Nove normas, marcador de procedência aplicado em todas.**

**Pendente:** Res. TRE-PR 959/2025 (IA) — sem referência própria. Nenhuma outra lacuna
estrutural identificada nesta rodada.

## 13. Res. TRE-PR 959/2025 incorporada — última pendência estrutural fechada (22/7/2026)
[[normas/ia-tre-pr-959-2025]]. Governança de IA na JE-PR, 22 artigos, publicada em
13/10/2025.

**🔴 ACHADO PRINCIPAL — os quatro prazos transitórios já venceram:** registro/inventário
no CGIA (30 dias → 12/11/2025), formulário de avaliação do CGIA (120 dias → 10/2/2026),
adequação gradual dos projetos existentes (180 dias → 11/4/2026) e processo de
estudos/pesquisa sem viés (180 dias → 11/4/2026). Todos vencidos entre 3 e 8 meses antes
de hoje. Diferente do padrão de "revisão de norma vencida" visto em outras peças do
ecossistema — aqui a pendência é factual e verificável: **o CGIA foi constituído? o
inventário existe? o formulário foi publicado?** Verificação prioritária registrada.

**🔴 ACHADO — CGIA fica fora do Sistema de Governança da Res. 932/2024.** O art. 4º, II
da 932/2024 lista taxativamente os Comitês (CGIC, CGTI, CGERI, CGJUD, CGO, CGSIPDP,
CGLGPAIS, CGRPNAP1J); o CGIA, criado por norma posterior, não consta do rol. O rito do
art. 6º, p.ú. da 932/2024 (Conselho de Governança → Corte) não foi expressamente
utilizado — o CGIA nasceu direto de Resolução da própria Corte, o que é válido, mas o
deixa fora do arcabouço procedimental comum (atas, relatório anual, regime de reuniões
dos demais Comitês). Periodicidade própria e mais exigente (trimestral, art. 5º, contra
o mínimo de 2/ano do art. 21, §2º da 932/2024).

**🔴 ACHADO — sobreposição não coordenada com o CGERI.** A Res. 980/2026 (posterior à
959/2025) deu ao CGERI competências de governança da inovação, incluindo priorizar
projetos de inovação (art. 11, XXI da 932/2024 pós-980). IA é inovação por definição;
nenhuma das duas normas menciona a outra. Um projeto de IA pode ser objeto de avaliação
pelo CGIA e de priorização pelo CGERI ao mesmo tempo, sem fronteira de competência
definida — lacuna de coordenação criada pela ordem cronológica das normas.

**Achado positivo — contraste de técnica legislativa:** os arts. 2º, 13 e 17, §2º usam
cláusula "ou outra que a venha substituir" ao citar Res. CNJ 615/2025, Res. TSE
23.644/2021 e Portaria CNJ 253/2020. Isso **resolve automaticamente** a obsolescência da
referência à 23.644/2021 (revogada) — ler como Res. TSE 23.763/2026 sem necessidade de
ressalva, diferente das referências mortas sem essa cláusula encontradas na PGPPDP
(art. 10, I) e na Res. 855/2020 (art. 31, III). Técnica a recomendar para as demais
normas do TRE-PR. Além disso, o art. 2º adota por remissão as definições da Res. CNJ
615/2025 em vez de criar glossário próprio — evita repetir o padrão de glossário órfão
já visto em PSI/PGPPDP/crises.

**Achado operacional direto — dever de rotulagem (art. 6º, §2º):** todo ato oficial
produzido com auxílio de IA deve identificar a ferramenta utilizada. Aplica-se a
qualquer documento produzido no exercício da função, potencialmente incluindo
documentos elaborados com apoio desta própria skill — vale conferir aplicação prática.

**Achado — RIPD de projeto de IA é discricionário (art. 17, §6º: "fica a critério do
Tribunal"), regime mais fraco que o da PGPPDP (art. 15, obrigatório quando envolve dado
pessoal). Registrado que, havendo dado pessoal no projeto de IA, prevalece o regime mais
protetivo da PGPPDP — a norma de IA não pode enfraquecer a proteção de dados já
estabelecida.

**Demais achados incorporados:** composição do CGIA (9 unidades); competências do
art. 4º; vedação de ambiente de desenvolvimento de IA fora do oficial (art. 7º, §3º);
propriedade intelectual de produção assistida por IA vinculada ao Tribunal, sem direito
autoral ao servidor (art. 17, §3º); padrão de auditabilidade mais flexível para IA que
para ativos de informação em geral (art. 14); prestação de contas anual com
transparência algorítmica ativa (art. 16, V).

`SKILL.md` e [[concepts/prazos-normativos-tre-pr]] atualizados com tema-chave e bloco de prazos vencidos.

## Estado final da auditoria (22/7/2026)
**Dez normas verificadas integralmente contra texto oficial, marcador de procedência em
todas:** Res. TSE 23.763/2026, Res. TSE 23.644/2021 (revogada), Portaria TSE 444/2021,
Res. TSE 23.650/2021 (PGPPDP), Res. TRE-PR 974/2026, Res. TRE-PR 932/2024, Res. TRE-PR
962/2025, Lei 12.527/2011, Res. TRE-PR 855/2020, Res. TRE-PR 959/2025.

**Nenhuma pendência estrutural conhecida remanescente.** Manutenção futura: acompanhar
a publicação da Estratégia Nacional de Cibersegurança (GT da Portaria TSE 294/2026), a
eventual revisão da 974/2026 (gatilho já disparado), e o cumprimento — ainda não
verificado in loco — dos prazos vencidos da 959/2025.
