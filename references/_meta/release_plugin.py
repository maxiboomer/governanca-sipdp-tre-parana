#!/usr/bin/env python3
"""Helper de release do plugin Claude.

Uso:
  python3 release_plugin.py            # bump patch (1.3.0 -> 1.3.1)
  python3 release_plugin.py minor      # bump minor (1.3.0 -> 1.4.0)
  python3 release_plugin.py major      # bump major (1.3.0 -> 2.0.0)

Mantém plugin.json, marketplace.json e a tag git em sincronia. O marketplace.json
é o índice que o Claude consulta para detectar atualização — nunca deixá-lo defasado.
"""
import json,re,sys,subprocess
from pathlib import Path
REPO=Path('/root/governanca-sipdp-tre-pr')
pj=REPO/'.claude-plugin/plugin.json'
mj=REPO/'.claude-plugin/marketplace.json'

def bump(v,part):
 major,minor,patch=map(int,v.split('.'))
 if part=='major': return f'{major+1}.0.0'
 if part=='minor': return f'{major}.{minor+1}.0'
 return f'{major}.{minor}.{patch+1}'

def main():
 part=sys.argv[1] if len(sys.argv)>1 else 'patch'
 data=json.loads(pj.read_text())
 cur=data['version']
 new=bump(cur,part)
 data['version']=new
 pj.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 # sync marketplace
 m=json.loads(mj.read_text())
 m['plugins'][0]['version']=new
 m['plugins'][0]['description']=data.get('description','')
 mj.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
 # git tag (não commita; só cria a tag local)
 subprocess.run(['git','-C',str(REPO),'add','-A'],check=False)
 print(f'plugin.json e marketplace.json: {cur} -> {new}')
 print('Agora: git commit -m "..." && git push && git tag v'+new+' && git push origin v'+new)

if __name__=='__main__':
 main()
