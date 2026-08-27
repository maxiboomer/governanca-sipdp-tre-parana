#!/usr/bin/env python3
"""Sincroniza vault -> build (repo de publicação).
Vault (/root/llmwiki/llm-wiki/wiki) é a fonte da verdade; este script gera/atualiza
references/ no repo /root/governanca-sipdp-tre-pr. raw/ não é copiado (já versionado).
"""
from pathlib import Path
import shutil,re
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
 'wiki/index.md':'references/index.md',
 'wiki/log.md':'references/log.md',
}
copied=0
for src_dir,dst in map_dirs.items():
 s=VAULT/src_dir
 if not s.exists(): continue
 if s.is_file():
  (REPO/dst).parent.mkdir(parents=True,exist_ok=True)
  shutil.copy2(s,REPO/dst); copied+=1; continue
 (REPO/dst).mkdir(parents=True,exist_ok=True)
 for f in list(s.glob('*.md'))+list(s.glob('*.py')):
  shutil.copy2(f,REPO/dst/f.name); copied+=1
# root meta files
for f in META:
 s=VAULT/f
 if s.exists(): shutil.copy2(s,REPO/f); copied+=1

# --- Sincronizar versão do plugin Claude ---
# plugin.json é a fonte da versão; marketplace.json é derivado (o Claude consulta o
# marketplace para detectar atualização). Mantê-los dessincronizados quebra o "atualizar".
import json
pj=REPO/'.claude-plugin/plugin.json'
mj=REPO/'.claude-plugin/marketplace.json'
if pj.exists() and mj.exists():
 try:
  pjv=json.loads(pj.read_text()).get('version')
  mdata=json.loads(mj.read_text())
  cur=mdata['plugins'][0].get('version')
  if pjv and pjv!=cur:
   mdata['plugins'][0]['version']=pjv
   # descrição do marketplace espelha a do plugin (se o plugin a tiver)
   pdesc=json.loads(pj.read_text()).get('description')
   if pdesc: mdata['plugins'][0]['description']=pdesc
   mj.write_text(json.dumps(mdata,ensure_ascii=False,indent=2)+'\n')
   print(f'  marketplace.json: {cur} -> {pjv}')
   copied+=1
  else:
   print(f'  marketplace.json já em {cur}')
 except Exception as e:
  print(f'  AVISO: falha ao sincronizar marketplace.json: {e}')

print(f'sincronizados {copied} arquivos vault->build')
