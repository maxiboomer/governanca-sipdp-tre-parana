# Acervo Normativo TRE-PR — SI/PDP

Base de normas internas do TRE-PR e da Justiça Eleitoral, mantida pela AGM, com uma camada
de curadoria voltada a Segurança da Informação e Proteção de Dados Pessoais. Existe para
responder, com citação verificável, o que a norma diz, se ela vale e quem é competente.

## Language

### O que o acervo guarda

**Norma**:
Ato normativo publicado, com veículo e data de publicação identificáveis. Sem publicação
identificada, o registro não é norma para este acervo — é instrumento monitorado.
_Avoid_: normativo, regramento, legislação interna

**Instrumento monitorado**:
Documento que a unidade acompanha mas que não é ato normativo publicado — plano interno,
documento de gestão, norma cuja existência não pôde ser verificada em repositório oficial.
Vive em lista própria, nunca na tabela de normas.
_Avoid_: norma interna, documento normativo

**Acervo**:
O conjunto completo de normas do TRE-PR e da JE reunidas aqui, de qualquer tema. Mais amplo
que SI/PDP por decisão registrada na ADR 0001.
_Avoid_: base, vault, biblioteca

**Camada curada**:
O subconjunto do acervo com síntese escrita — competências, prazos, efeitos. Recorte de
SI/PDP, continuidade e governança. O resto do acervo existe como texto, sem síntese.
_Avoid_: wiki, páginas boas

### Sobre a verdade de uma norma

**Publicação**:
Veículo, número, data e página em que a norma saiu — DJE-TRE-PR, DJE-TSE, DOU. É o que
sustenta qualquer afirmação sobre a norma.
_Avoid_: fonte, referência, origem

**Situação da norma**:
Vigente, Revogada ou Alterada. Só é afirmável com a publicação que a sustenta: a publicação
da própria norma, ou a da norma que a revogou ou alterou.
_Avoid_: status, vigência (como rótulo de campo), situação

**Fonte da verdade**:
A publicação oficial. Nem o inventário deste acervo nem a planilha da SECTI são autoridade
sobre situação de norma — ambos são índices que apontam para a publicação.
_Avoid_: fonte oficial, base autoritativa

**Inventário**:
Índice de normas com sua situação e a publicação que a sustenta. Instrumento de busca, não
de prova.
_Avoid_: planilha, controle, tabela mestre

### Sobre o estado de cada página

**Página curada**:
Página com síntese escrita da norma. Afirma competências, prazos e efeitos, citando artigo.
_Avoid_: página pronta, página completa

**Página não curada**:
Marcador que aponta para o texto da norma sem sintetizá-lo. Marcada `curadoria: pendente`.
Não é ausência de informação — a informação está no texto que ela indica.
_Avoid_: página vazia, stub, placeholder

**Texto da norma**:
O conteúdo normativo em `references/raw/`. Camada imutável. Nem sempre integral: alguns
registros são excertos, e isso precisa estar declarado na página.
_Avoid_: raw, fonte primária, texto integral

### Quem usa

**AGM**:
Assessoria Técnica de Governança e Monitoramento da Segurança da Informação. Unidade dona
deste acervo e sua consumidora. Ver `references/entities/agm.md`.
_Avoid_: assessoria, unidade de governança
