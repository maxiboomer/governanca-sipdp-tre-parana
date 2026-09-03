#!/usr/bin/env python3
"""Sincroniza vault -> build (repo de publicação / plugin Claude).

Vault (/root/llmwiki/llm-wiki/wiki) é a fonte da verdade; este script gera/atualiza
a ÚNICA cópia de references/ dentro da skill em
/root/governanca-sipdp-tre-pr/skills/governanca-sipdp-tre-pr/references/.

A raiz do repo NÃO mantém references/ (removido em 2026-09-02): a skill só lê a cópia
interna, e a duplicação dobrou o tamanho do plugin e divergiu (a interna ficou
desatualizada). Caminho único elimina o problema.

Reescrita de links: o vault usa wikilinks Obsidian [[wiki/...]] e caminhos `raw/...`;
no build, os links viram [[references/...]] e `references/raw/...` (convenção do
SKILL.md: caminho a partir da raiz da skill).
"""
from pathlib import Path
import shutil, re, json
VAULT = Path('/root/llmwiki/llm-wiki')
REPO = Path('/root/governanca-sipdp-tre-pr')
SKILL_DIR = REPO / 'skills/governanca-sipdp-tre-pr'
SKILL_REF = SKILL_DIR / 'references'
META = ['SCHEMA.md', 'CLAUDE.md', 'CONTEXT.md', 'README.md']

# Origem no vault -> destino dentro da skill (references/)
map_dirs = {
    'wiki/normas':      'normas',
    'wiki/entities':    'entities',
    'wiki/concepts':    'concepts',
    'wiki/inventarios': 'inventarios',
    'wiki/sources':     'sources',
    'wiki/comparisons': 'comparisons',
    'wiki/_meta':       '_meta',
    'raw':              'raw',
    'wiki/raw':         'raw',
    'wiki/index.md':    'index.md',
    'wiki/log.md':      'log.md',
}


def rewrite_links(txt):
    """Converte caminhos do vault em caminhos do plugin (build).

    Mantém o vault intocado; aplica-se apenas à cópia do build.
    - [[wiki/...]]        -> [[references/...]]
    - `wiki/_meta/...`    -> `references/_meta/...` (backtick)
    - `raw/...`           -> `references/raw/...`   (backtick)
    - (raw/... e (wiki/.. -> (references/...        (markdown link)
    - sources: [raw/...]  -> sources: [references/raw/...] (frontmatter)
    """
    txt = txt.replace('[[wiki/', '[[references/')
    txt = txt.replace('`wiki/', '`references/')
    txt = txt.replace('`raw/', '`references/raw/')
    txt = txt.replace('(wiki/', '(references/')
    txt = txt.replace('(raw/', '(references/raw/')
    txt = txt.replace('sources: [raw/', 'sources: [references/raw/')
    return txt


def copytree(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_file():
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix == '.md':
            (dst).write_text(rewrite_links(src.read_text(encoding='utf-8')), encoding='utf-8')
        else:
            shutil.copy2(src, dst)
        return 1
    dst.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in list(src.glob('*.md')) + list(src.glob('*.py')):
        if f.suffix == '.md':
            (dst / f.name).write_text(rewrite_links(f.read_text(encoding='utf-8')), encoding='utf-8')
        else:
            shutil.copy2(f, dst / f.name)
        n += 1
    return n


copied = 0
for src_rel, dst_rel in map_dirs.items():
    s = VAULT / src_rel
    if s.exists():
        copied += copytree(s, SKILL_REF / dst_rel)

# META na raiz da skill (SKILL.md, CONTEXT.md, CLAUDE.md, SCHEMA.md)
for f in META:
    s = VAULT / f
    if s.exists():
        txt = s.read_text(encoding='utf-8')
        if f.endswith('.md'):
            txt = rewrite_links(txt)
        (SKILL_DIR / f).write_text(txt, encoding='utf-8')
        copied += 1

# ADRs: fonte é o repo (docs/adr), copiar para dentro da skill (docs/adr)
adr_src = REPO / 'docs/adr'
adr_dst = SKILL_DIR / 'docs/adr'
if adr_src.exists():
    adr_dst.mkdir(parents=True, exist_ok=True)
    for f in sorted(adr_src.glob('*.md')):
        shutil.copy2(f, adr_dst / f.name)
        copied += 1

# SKILL.md é mantido manualmente no repo (não existe no vault); não sobrescrever.

# --- Sincronizar versão do plugin Claude ---
pj = REPO / '.claude-plugin/plugin.json'
mj = REPO / '.claude-plugin/marketplace.json'
if pj.exists() and mj.exists():
    try:
        pjv = json.loads(pj.read_text()).get('version')
        mdata = json.loads(mj.read_text())
        cur = mdata['plugins'][0].get('version')
        if pjv and pjv != cur:
            mdata['plugins'][0]['version'] = pjv
            pdesc = json.loads(pj.read_text()).get('description')
            if pdesc:
                mdata['plugins'][0]['description'] = pdesc
            mj.write_text(json.dumps(mdata, ensure_ascii=False, indent=2) + '\n')
            print(f'  marketplace.json: {cur} -> {pjv}')
            copied += 1
        else:
            print(f'  marketplace.json já em {cur}')
    except Exception as e:
        print(f'  AVISO: falha ao sincronizar marketplace.json: {e}')

print(f'sincronizados {copied} arquivos vault->build (cópia única em skills/governanca-sipdp-tre-pr/references/)')
