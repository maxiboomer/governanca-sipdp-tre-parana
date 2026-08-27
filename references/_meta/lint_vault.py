#!/usr/bin/env python3
from pathlib import Path
import re,os,json,collections
W=Path(__file__).resolve().parents[2]
files=[p for p in (W/'wiki').rglob('*.md')]
rel=lambda p:p.relative_to(W).as_posix()
existing={rel(p)[:-3] for p in files}
# resolver allows Obsidian extensionless links and basename aliases
raw_existing={rel(p)[:-3] for p in (W/'raw').rglob('*.md')}
links=[]; broken=[]; indexed=set(re.findall(r'\[\[([^\]|#]+)',(W/'wiki'/'index.md').read_text(errors='ignore')))
for p in files:
 t=p.read_text(errors='ignore')
 for l in re.findall(r'\[\[([^\]|#]+)',t):
  if l.startswith('wiki/'):
   if l not in existing and l+'.md' not in existing: broken.append([rel(p),l])
  elif l.startswith('raw/'):
   if l not in raw_existing and l+'.md' not in raw_existing: broken.append([rel(p),l])
  links.append([rel(p),l])
stubs=[]; missing=[]; fields=[]; badlinks=[]
for p in files:
 if p.name in ('index.md','log.md'): continue  # arquivos administrativos, sem frontmatter obrigatório
 t=p.read_text(errors='ignore'); fm=t.split('---',2)[1] if t.startswith('---') else ''
 for k in ['title','created','updated','type','status','curadoria','escopo','tags']:
  if not re.search(r'^'+k+r':',fm,re.M): fields.append([rel(p),k])
 # curadoria vem do frontmatter (fonte única), não de heurística de texto
 cm=re.search(r'^curadoria:\s*"?([^"\n]+?)"?\s*$',fm,re.M)
 curado=cm.group(1).strip() if cm else ''
 if curado in ('stub','pendente'): stubs.append(rel(p))
 # wikilinks com prefixo errado (references/) quebram o vault
 for l in re.findall(r'\[\[references/[^\]|#]+',t): badlinks.append([rel(p),l])
for p in files:
 if rel(p).startswith('wiki/') and rel(p)!='wiki/index.md' and rel(p)!='wiki/log.md' and rel(p)[:-3] not in indexed: missing.append(rel(p))
print(json.dumps({'pages':len(files),'broken_links':broken,'index_missing':missing,'field_issues':fields,'stubs':stubs,'bad_wikilink_prefix':badlinks},ensure_ascii=False,indent=2))
