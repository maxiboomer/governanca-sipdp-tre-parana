# governanca-sipdp-tre-pr

Acervo de **normas internas do TRE-PR e da Justiça Eleitoral**, mantido pela AGM
(Assessoria Técnica de Governança e Monitoramento da Segurança da Informação), com uma
camada curada de Segurança da Informação, Proteção de Dados Pessoais e continuidade.

O vocabulário do domínio está em [`CONTEXT.md`](./CONTEXT.md). As decisões de desenho estão
em [`docs/adr/`](./docs/adr/).

## Escopo

O acervo é amplo — normas do TRE-PR de qualquer tema, inclusive sem relação com SI/PDP. O
recorte de SI/PDP é a camada de curadoria, não o acervo. Ver
[ADR 0001](./docs/adr/0001-escopo-amplo-com-camada-curada.md).

## O que tem dentro

- **PSI nacional** — Res. TSE 23.763/2026 (e a revogada 23.644/2021 como histórico)
- **PSI local** — Res. TRE-PR 974/2026
- **LGPD/PDP** — fundamentos, framework documental, fases 1–2, maturidade, IA & LGPD, PGPPDP
- **Estrutura orgânica** — Res. 982/2026, Res. 971/2026, AGM, CGSI/PDP, Encarregado/DPO,
  ETIR, ASC, SECTI, Comitê de Crises Cibernéticas (932/2024 e 962/2025)
- **Continuidade** — PGCN (Port. 302/2025) e Protocolo Socioambiental (Port. 056/2026)
- **Prazos consolidados** e inventários de vigência (TRE-PR/TSE e CNJ)
- **Normas técnicas SECTI** — nuvem, projetos, segurança Linux, desenvolvimento, orçamento

## Estrutura

```
SKILL.md                          entrada da skill
CONTEXT.md                        glossário do domínio
docs/adr/                         decisões de desenho
references/index.md               catálogo (200 páginas)
references/normas/         168    página por norma
references/entities/         8    AGM, CGSI/PDP, ETIR, ASC, DPO, SECTI, ANPD, CSI
references/concepts/        13    LGPD, continuidade, prazos, monitoramento SECTI
references/inventarios/      4    vigências TRE-PR/TSE e CNJ, lacunas, instrumentos monitorados
references/sources/          7    sínteses por tipo de norma
references/raw/            158    textos das normas (camada imutável)
references/_meta/            6    matriz de verificação, classificação, pendências, qualidade
```

## Regra de sustentação

Nem o inventário deste acervo nem a planilha da SECTI são autoridade sobre vigência — a
verdade é a publicação oficial. Ver
[ADR 0002](./docs/adr/0002-dje-como-fonte-da-verdade.md).

Cada linha do inventário declara a situação da norma e o que a sustenta, em três níveis:
citação de DJE/DOU (basta para citar em documento) → compilado oficial (serve para
trabalhar) → nada, e então a situação é **Não confirmada**.

Situação nas páginas de normas (metadados curados):
- **vigentes:** 78 com publicação oficial localizada ou compilado confirmado
- **revogadas:** 17 com revogação expressa no texto ou em norma posterior
- **não-confirmadas:** 58 sem confirmação individual até o momento
- **outros:** 15 (históricas, de composição, etc.)

A matriz completa está em `references/_meta/matriz-verificacao-vigencia.md`.

## Estado de curadoria — leia antes de confiar

- **54 das 168 páginas de `references/normas/` estão totalmente curadas** — têm síntese,
  obrigações, papéis, relações e status documentado. As demais 113 permanecem como stub
  (`curadoria: stub`), com metadados normalizados e texto bruto preservado em
  `references/raw/`.
- Os 14 temas classificados como `central-si-pdp` (PSI, ETIR, CSTI, gestão de riscos, PSI
  local, comitês) já foram curados integralmente.
- **Nem todo arquivo de `raw/` é texto integral.** A Res. 971/2026 está como excerto (~2 KB
  de um original de ~277 mil caracteres). Os Anexos I e II da Res. 982/2026 não constam.
- **Lacunas do inventário** mapeadas em
  `references/inventarios/lacunas-do-inventario.md`: 31 normas do acervo sem linha no
  inventário TRE-PR/TSE, e Res. CNJ 433/2021 e 646/2025 ausentes do inventário CNJ.
- **Classificação dos stubs** em `references/_meta/classificacao-normas.md`: 14 centrais
  (curados), 39 apoio governança, 53 contextual, 22 fora de escopo.

## Convenção de caminhos

Todo link interno é caminho a partir da raiz do plugin
(`references/normas/psi-tse-23763-2026.md`), não wikilink de vault.

## Fontes

Normas publicadas nos portais do TRE-PR, TSE e CNJ.
