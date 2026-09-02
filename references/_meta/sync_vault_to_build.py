#!/usr/bin/env python3
"""Sincroniza vault -> build (repo de publicação / plugin Claude).
Vault (/root/llmwiki/llm-wiki/wiki) é a fonte da verdade; este script gera/atualiza
references/ no repo /root/governanca-sipdp-tre-pr. O repo INTEIRO é o plugin:
SKILL.md na raiz + .claude-plugin/plugin.json único + references/.
raw/ não é copiado (já versionado).
"""
from pathlib import Path
import shutil,re,json
VAULT=Path('/root/llmwiki/llm-wiki')
REPO=Path('/root/governanca-sipdp-tre-pr')
META=['SCHEMA.md','CLAUDE.md','CONTEXT.md','SKILL.md','README.md']
map_dirs={
 'wiki/normas':'references/normas',
 'wiki/entities':'references/entities',
 'wiki/concepts':'references/concepts',
 'wiki/inventarios':'references/inventarios',
 'wiki/sources':'references/sources',
 'wiki/_meta':'references/_meta',
 'raw':'references/raw',
 'wiki/raw':'references/raw',
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
for src_dir,dst in map_dirs.items():
 s=VAULT/src_dir
 if s.exists():
  copied+=copytree(s, REPO/dst)
for f in META:
 s=VAULT/f
 if s.exists(): shutil.copy2(s,REPO/f); copied+=1

# Copiar references também para dentro da skill (skills/<nome>/references/)
SKILL_REF=REPO/'skills/governanca-sipdp-tre-pr/references'
SKILL_DIR=REPO/'skills/governanca-sipdp-tre-pr'
for src_dir in ['normas','entities','concepts','inventarios','sources','_meta']:
 s=VAULT/'wiki'/src_dir
 if s.exists(): copied+=copytree(s, SKILL_REF/src_dir)
for f,sub in [('wiki/index.md','index.md'),('wiki/log.md','log.md'),('SCHEMA.md','SCHEMA.md')]:
 s=VAULT/f
 if s.exists(): shutil.copy2(s, SKILL_REF/sub); copied+=1
# SKILL.md e CONTEXT/CLAUDE dentro da skill
for f in ['SKILL.md','CONTEXT.md','CLAUDE.md']:
 s=VAULT/f
 if s.exists(): shutil.copy2(s, SKILL_DIR/f); copied+=1

# --- Sincronizar versão do plugin Claude (arquivo único .claude-plugin/plugin.json) ---
pj=REPO/'.claude-plugin/plugin.json'
mj=REPO/'.claude-plugin/marketplace.json'
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
 except Exception as e:
  print(f'  AVISO: falha ao sincronizar marketplace.json: {e}')

print(f'sincronizados {copied} arquivos vault->build')
