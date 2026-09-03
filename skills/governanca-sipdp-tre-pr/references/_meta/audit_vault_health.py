#!/usr/bin/env python3
"""
audit_vault_health.py — Auditoria de saúde do acervo de normas.

Verifica:
1. Cobertura de raws (normas com raw existente vs. faltante)
2. Raws órfãos (raw sem norma correspondente)
3. Normas sem raw (drift de rastreabilidade)
4. Links quebrados (wikilinks inválidos)
5. Frontmatter (confidence, sha256, source_url)
6. Status (vigente, revogada, etc.)

Uso:
    python3 _meta/audit_vault_health.py [--json] [--report]
"""

import os
import re
import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime

# Configuração
VAULT_DIR = Path(__file__).parent.parent
NORMAS_DIR = VAULT_DIR / "normas"
RAW_DIR = VAULT_DIR.parent / "raw"  # /root/llmwiki/llm-wiki/raw/
ENTITIES_DIR = VAULT_DIR / "entities"
CONCEPTS_DIR = VAULT_DIR / "concepts"
COMPARISONS_DIR = VAULT_DIR / "comparisons"
INVENTARIOS_DIR = VAULT_DIR / "inventarios"

# Padrões de slug para raw
RAW_SLUG_MAP = {
    "cnj-resolucao-363-2021": "cnj-resolucao-363-2021.md",
    "governanca-e-crises-tre-pr": "governanca-e-crises-tre-pr.md",
    "ia-tre-pr-959-2025": "ia-tre-pr-959-2025.md",
    "lai-12527-2011": "lai-12527-2011.md",
    "portaria-tre-pr-302-2025": "portaria-tre-pr-302-2025.md",
    "psi-termos-portaria-tse-444-2021": "psi-termos-portaria-tse-444-2021.md",
    "psi-tre-pr-974-2026": "psi-tre-pr-974-2026.md",
    "psi-tse-23644-2021-revogada": "psi-tse-23644-2021-revogada.md",
    "psi-tse-23763-2026": "psi-tse-23763-2026.md",
    "resolucao-tre-pr-962-2025": "resolucao-tre-pr-962-2025.md",
}


def read_frontmatter(filepath):
    """Lê o frontmatter YAML de um arquivo markdown."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content.startswith('---'):
            return {}
        end = content.find('---', 3)
        if end == -1:
            return {}
        fm_text = content[3:end].strip()
        fm = {}
        for line in fm_text.split('\n'):
            if ':' in line:
                key, _, value = line.partition(':')
                key = key.strip()
                value = value.strip()
                # Remove aspas
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]
                # Tenta parsear listas
                if value.startswith('[') and value.endswith(']'):
                    value = [v.strip().strip('"').strip("'") for v in value[1:-1].split(',') if v.strip()]
                fm[key] = value
        return fm
    except Exception as e:
        return {"_error": str(e)}


def compute_sha256(filepath):
    """Calcula SHA256 de um arquivo."""
    try:
        with open(filepath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return None


def find_raw_for_norma(norma_slug):
    """Encontra o raw correspondente a uma norma."""
    # Mapeamento direto de nomes de arquivo
    raw_name = norma_slug + ".md"
    raw_path = RAW_DIR / raw_name
    if raw_path.exists():
        return str(raw_path)
    
    # Busca por padrões comuns
    for f in RAW_DIR.glob("*.md"):
        if f.stem.startswith(norma_slug[:20]):
            return str(f)
    
    return None


def audit_coverage():
    """Verifica cobertura de raws."""
    normas = list(NORMAS_DIR.glob("*.md"))
    raws = list(RAW_DIR.glob("*.md"))
    
    normas_with_raw = []
    normas_without_raw = []
    raws_orphaned = []
    
    # Mapeia raws por slug
    raw_slugs = {f.stem: f for f in raws}
    raw_used = set()
    
    for norma in normas:
        fm = read_frontmatter(norma)
        sources = fm.get('sources', [])
        if isinstance(sources, str):
            sources = [sources]
        
        found_raw = None
        for src in sources:
            if 'raw/' in src:
                raw_path = VAULT_DIR / src
                if raw_path.exists():
                    found_raw = src
                    raw_used.add(raw_path.stem)
                else:
                    # Tenta encontrar por correspondência parcial
                    for raw_slug, raw_file in raw_slugs.items():
                        if raw_slug in src or src.split('/')[-1].replace('.md', '') in raw_slug:
                            found_raw = str(raw_file)
                            raw_used.add(raw_slug)
                            break
        
        if found_raw:
            normas_with_raw.append({
                'norma': str(norma.name),
                'raw': found_raw,
                'status': fm.get('status', 'unknown')
            })
        else:
            normas_without_raw.append({
                'norma': str(norma.name),
                'raw_declared': sources,
                'status': fm.get('status', 'unknown')
            })
    
    # Raws órfãos (não referenciados por nenhuma norma)
    for raw_slug, raw_file in raw_slugs.items():
        if raw_slug not in raw_used:
            # Verifica se é um raw de entidade/concept/comparison
            if raw_slug not in ['INVENTARIO-NORMAS-COLETADAS', 'README', 'Sem título']:
                raws_orphaned.append(str(raw_file.name))
    
    return {
        'total_normas': len(normas),
        'total_raws': len(raws),
        'normas_with_raw': normas_with_raw,
        'normas_without_raw': normas_without_raw,
        'raws_orphaned': raws_orphaned,
        'coverage_pct': round(len(normas_with_raw) / len(normas) * 100, 1) if normas else 0
    }


def audit_frontmatter():
    """Verifica qualidade do frontmatter."""
    issues = []
    stats = {
        'total': 0,
        'with_confidence': 0,
        'with_sha256': 0,
        'with_source_url': 0,
        'with_status': 0,
        'status_counts': {},
        'confidence_counts': {}
    }
    
    for norma in NORMAS_DIR.glob("*.md"):
        stats['total'] += 1
        fm = read_frontmatter(norma)
        
        # Verifica campos obrigatórios
        if 'confidence' in fm:
            stats['with_confidence'] += 1
            conf = fm['confidence']
            stats['confidence_counts'][conf] = stats['confidence_counts'].get(conf, 0) + 1
        else:
            if fm.get('escopo') == 'central-si-pdp':
                issues.append({
                    'file': str(norma.name),
                    'issue': 'missing_confidence',
                    'detail': 'Norma central sem campo confidence'
                })
        
        if 'sha256' in fm:
            stats['with_sha256'] += 1
        
        if 'source_url' in fm:
            stats['with_source_url'] += 1
        
        if 'status' in fm:
            stats['with_status'] += 1
            status = fm['status']
            stats['status_counts'][status] = stats['status_counts'].get(status, 0) + 1
        else:
            issues.append({
                'file': str(norma.name),
                'issue': 'missing_status',
                'detail': 'Norma sem campo status'
            })
    
    return {'stats': stats, 'issues': issues}


def audit_links():
    """Verifica links quebrados (wikilinks)."""
    broken = []
    all_pages = set()
    
    # Coleta todas as páginas
    for d in [NORMAS_DIR, ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR, INVENTARIOS_DIR]:
        if d.exists():
            for f in d.glob("*.md"):
                all_pages.add(f.stem)
    
    # Verifica links em normas
    for norma in NORMAS_DIR.glob("*.md"):
        with open(norma, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Encontra wikilinks [[...]]
        links = re.findall(r'\[\[([^\]]+)\]\]', content)
        for link in links:
            # Remove alias se houver
            target = link.split('|')[0].strip()
            # Remove prefixo wiki/ se houver
            if target.startswith('wiki/'):
                target = target[5:]
            # Verifica se a página existe
            if target and target not in all_pages:
                # Verifica se é um raw
                if not (RAW_DIR / f"{target}.md").exists():
                    broken.append({
                        'source': str(norma.name),
                        'target': target,
                        'link': link
                    })
    
    return broken


def generate_report(coverage, frontmatter, links):
    """Gera relatório consolidado."""
    report = {
        'timestamp': datetime.now().isoformat(),
        'summary': {
            'total_normas': coverage['total_normas'],
            'total_raws': coverage['total_raws'],
            'raw_coverage_pct': coverage['coverage_pct'],
            'normas_with_raw': len(coverage['normas_with_raw']),
            'normas_without_raw': len(coverage['normas_without_raw']),
            'raws_orphaned': len(coverage['raws_orphaned']),
            'broken_links': len(links),
            'frontmatter_issues': len(frontmatter['issues'])
        },
        'coverage': coverage,
        'frontmatter': frontmatter,
        'broken_links': links
    }
    
    return report


def format_markdown_report(report):
    """Formata relatório em markdown."""
    s = report['summary']
    c = report['coverage']
    f = report['frontmatter']
    
    md = f"""# 🏥 Saúde do Acervo — {report['timestamp'][:10]}

## Resumo

| Métrica | Valor |
|---|---|
| Total normas | {s['total_normas']} |
| Total raws | {s['total_raws']} |
| Cobertura de raws | {s['raw_coverage_pct']}% |
| Normas com raw | {s['normas_with_raw']} |
| Normas sem raw | {s['normas_without_raw']} |
| Raws órfãos | {s['raws_orphaned']} |
| Links quebrados | {s['broken_links']} |
| Issues frontmatter | {s['frontmatter_issues']} |

## Status das normas

| Status | Quantidade |
|---|---|
"""
    for status, count in sorted(f['stats'].get('status_counts', {}).items()):
        md += f"| {status} | {count} |\n"
    
    md += "\n## Confidence\n\n| Nível | Quantidade |\n|---|---|\n"
    for conf, count in sorted(f['stats'].get('confidence_counts', {}).items()):
        md += f"| {conf} | {count} |\n"
    
    if c['normas_without_raw']:
        md += "\n## ⚠️ Normas sem raw (drift de rastreabilidade)\n\n| Norma | Raw declarado | Status |\n|---|---|---|\n"
        for item in c['normas_without_raw']:
            raw_declared = ', '.join(item['raw_declared']) if isinstance(item['raw_declared'], list) else str(item['raw_declared'])
            md += f"| {item['norma']} | {raw_declared} | {item['status']} |\n"
    
    if c['raws_orphaned']:
        md += "\n## ⚠️ Raws órfãos\n\n| Raw |\n|---|---|\n"
        for raw in c['raws_orphaned']:
            md += f"| {raw} |\n"
    
    if report['broken_links']:
        md += "\n## ⚠️ Links quebrados\n\n| Origem | Destino |\n|---|---|\n"
        for link in report['broken_links'][:50]:  # Limita a 50
            md += f"| {link['source']} | {link['target']} |\n"
        if len(report['broken_links']) > 50:
            md += f"| ... | +{len(report['broken_links'])-50} |\n"
    
    if f['issues']:
        md += "\n## ⚠️ Issues de frontmatter\n\n| Arquivo | Problema | Detalhe |\n|---|---|---|\n"
        for issue in f['issues']:
            md += f"| {issue['file']} | {issue['issue']} | {issue['detail']} |\n"
    
    return md


def main():
    args = sys.argv[1:]
    
    print("🔍 Auditando saúde do acervo...")
    
    coverage = audit_coverage()
    frontmatter = audit_frontmatter()
    links = audit_links()
    
    report = generate_report(coverage, frontmatter, links)
    
    if '--json':
        print(json.dumps(report, indent=2, ensure_ascii=False))
    elif '--report' in args:
        md = format_markdown_report(report)
        report_path = VAULT_DIR / "_meta" / "health_report.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f"Relatório salvo em: {report_path}")
        print(md)
    else:
        # Saída resumida
        s = report['summary']
        print(f"\n📊 Resumo:")
        print(f"  Normas: {s['total_normas']} | Raws: {s['total_raws']} | Cobertura: {s['raw_coverage_pct']}%")
        print(f"  Sem raw: {s['normas_without_raw']} | Órfãos: {s['raws_orphaned']} | Links quebrados: {s['broken_links']}")
        print(f"  Issues frontmatter: {s['frontmatter_issues']}")
        
        if coverage['normas_without_raw']:
            print(f"\n⚠️  Normas sem raw:")
            for item in coverage['normas_without_raw']:
                print(f"  - {item['norma']}")
        
        if coverage['raws_orphaned']:
            print(f"\n⚠️  Raws órfãos:")
            for raw in coverage['raws_orphaned']:
                print(f"  - {raw}")
        
        if frontmatter['issues']:
            print(f"\n⚠️  Issues de frontmatter:")
            for issue in frontmatter['issues']:
                print(f"  - {issue['file']}: {issue['issue']}")
    
    # Exit code: 0 = saudável, 1 = problemas encontrados
    if s['normas_without_raw'] > 0 or s['broken_links'] > 0 or s['frontmatter_issues'] > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
