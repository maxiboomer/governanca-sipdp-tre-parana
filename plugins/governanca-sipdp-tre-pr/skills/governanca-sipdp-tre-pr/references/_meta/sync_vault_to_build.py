#!/usr/bin/env python3
"""Sincroniza vault -> build (repo de publicação / plugin Claude).
Vault (/root/llmwiki/llm-wiki/wiki) é a fonte da verdade; este script gera/atualiza:
  1. references/ no repo (estrutura legada)
  2. plugins/governanca-sipdp-tre-pr/skills/governanca-sipdp-tre-pr/references/
     (estrutura oficial de plugin Claude — onde o claude.ai procura o conteúdo)
raw/ não é copiado (já versionado).
"""
from pathlib import Path
import shutil,re,json
VAULT=Path('/root/llmwiki/llm-wiki')
REPO=Path('/root/governanca-sipdp-tre-pr')
META=['SCHEMA.md','CLAUDE.md','CONTEXT.md','SKILL.md','README.md']
# Destinos das references: estrutura legada + estrutura de plugin
PLUGIN_REF=REPO/'plugins/governanca-sipdp-tre-pr/skills/governanca-sipdp-tre-pr/references'
PLUGIN_SKILL=REPO/'plugins/governanca-sipdp-tre-pr/skills/governanca-sipdp-tre-pr'
map_dirs={
 'wiki/normas':'references/normas',
 'wiki/entities':'references/entities',
 'wiki/concepts':'references/concepts',
 'wiki/inventarios':'references/inventarios',
 'wiki/sources':'references/sources',
 'wiki/_meta':'references/_meta',
 'wiki/index.md':'references/index.md',
 'wiki/log.md':'references/log.md',
}
def copytree(src, dst):
 dst.parent.mkdir(parents=True,exist_ok=True)
 if src.is_file():
  dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dst); return 1
 dst.mkdir(parents=True,exist_ok=True)
 n=0
 for f in list(src.glob('*.md'))+list(src.glob('*.py')):
  shutil.copy2(f,dst/f.name); n+=1
 return n
copied=0
# 1. estrutura legada
for src_dir,dst in map_dirs.items():
 s=VAULT/src_dir
 if s.exists():
  copied+=copytree(s, REPO/dst)
for f in META:
 s=VAULT/f
 if s.exists(): shutil.copy2(s,REPO/f); copied+=1
# 2. estrutura de plugin (oficial) — references + meta dentro da skill
for src_dir in ['normas','entities','concepts','inventarios','sources','_meta']:
 s=VAULT/'wiki'/src_dir
 if s.exists(): copied+=copytree(s, PLUGIN_REF/src_dir)
for f,sub in [('wiki/index.md','index.md'),('wiki/log.md','log.md'),('SCHEMA.md','SCHEMA.md')]:
 s=VAULT/f
 if s.exists(): shutil.copy2(s, PLUGIN_REF/sub); copied+=1
# SKILL.md e CONTEXT/CLAUDE na skill
for f in ['SKILL.md','CONTEXT.md','CLAUDE.md']:
 s=VAULT/f
 if s.exists(): shutil.copy2(s, PLUGIN_SKILL/f); copied+=1

# --- Sincronizar versão do plugin Claude ---
pj=REPO/'.claude-plugin/plugin.json'
mj=REPO/'.claude-plugin/marketplace.json'
pjp=PLUGIN_SKILL.parent.parent/'.claude-plugin/plugin.json'
if pj.exists() and mj.exists():
 try:
  pjv=json.loads(pj.read_text()).get('version')
  mdata=json.loads(mj.read_text())
  cur=mdata['plugins'][0].get('version')
  if pjv and pjv!=cur:
   mdata['plugins'][0]['version']=pjv
   pdesc=json.loads(pj.read_text()).get('description')
   if pdesc: mdata['plugins'][0]['description']=pdesc
   mj.write_text(json.dumps(mdata,ensure_ascii=False,indent=2)+'\n')
   print(f'  marketplace.json: {cur} -> {pjv}'); copied+=1
  else:
   print(f'  marketplace.json já em {cur}')
  # sync versão no plugin.json interno
  if pjp.exists():
   inner=json.loads(pjp.read_text())
   if inner.get('version')!=pjv:
    inner['version']=pjv; pjp.write_text(json.dumps(inner,ensure_ascii=False,indent=2)+'\n')
    print(f'  plugin interno -> {pjv}')
 except Exception as e:
  print(f'  AVISO: falha ao sincronizar marketplace.json: {e}')

print(f'sincronizados {copied} arquivos vault->build')
