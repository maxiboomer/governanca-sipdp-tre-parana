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

## Estrutura

```
SKILL.md                          entrada da skill
CONTEXT.md                        glossário do domínio
docs/adr/                         decisões de desenho
references/index.md               catálogo (197 páginas)
references/normas/         165    página por norma
references/entities/         8    AGM, CGSI/PDP, ETIR, ASC, DPO, SECTI, ANPD, CSI
references/concepts/        13    LGPD, continuidade, prazos, monitoramento SECTI
references/inventarios/      4    vigências TRE-PR/TSE e CNJ, lacunas, instrumentos monitorados
references/sources/          7    sínteses por tipo de norma
references/raw/            154    textos das normas (camada imutável)
```

## Regra de sustentação

Nem o inventário deste acervo nem a planilha da SECTI são autoridade sobre vigência — a
verdade é a publicação oficial. Ver
[ADR 0002](./docs/adr/0002-dje-como-fonte-da-verdade.md).

Cada linha do inventário declara a situação da norma e o que a sustenta, em três níveis:
citação de DJE/DOU (basta para citar em documento) → compilado oficial (serve para
trabalhar) → nada, e então a situação é **Não confirmada**.

Hoje: 83 vigentes, 20 revogadas, 1 não confirmada.

## Estado de curadoria — leia antes de confiar

- **144 das 165 páginas de `references/normas/` não têm síntese escrita.** São marcadores
  com `curadoria: pendente` no frontmatter, que apontam para o texto em `references/raw/`.
  A informação existe; a síntese não. O `SKILL.md` instrui a ler o texto nesses casos.
  Para listar o que falta: `grep -l "curadoria: pendente" references/normas/*.md`
- **Nem todo arquivo de `raw/` é texto integral.** A Res. 971/2026 está como excerto (~2 KB
  de um original de ~277 mil caracteres). Os Anexos I e II da Res. 982/2026 não constam.
- **Lacunas do inventário** mapeadas em
  `references/inventarios/lacunas-do-inventario.md`: 31 normas do acervo sem linha no
  inventário TRE-PR/TSE, e Res. CNJ 433/2021 e 646/2025 ausentes do inventário CNJ.

## Convenção de caminhos

Todo link interno é caminho a partir da raiz do plugin
(`references/normas/psi-tse-23763-2026.md`), não wikilink de vault.

## Fontes

Normas publicadas nos portais do TRE-PR, TSE e CNJ.
