#!/usr/bin/env python3
"""Monitoramento normativo report-only (guiado).

O acesso direto via urllib é bloqueado (HTTP 403) pelos portais TRE-PR/TSE/CNJ.
Este script documenta as fontes e gera o relatório-base; o acionamento real do
monitoramento (coleta das listagens oficiais) usa o serviço de extração web da
plataforma, que resolve como navegador.

Modo de uso:
  - Sob demanda: o agente roda a extração das listagens oficiais e registra o
    diff contra o vault em wiki/_meta/relatorio-monitoramento.md.
  - Este script imprime o estado das fontes e o inventário esperado, como
    referência estável para cron/automação.

Nunca altera o vault automaticamente (report-only).
"""
from pathlib import Path
W = Path(__file__).resolve().parents[2]

# Fontes oficiais de listagens compiladas (para extração web / navegador)
SOURCES = {
    "TRE-PR Resoluções": "https://www.tre-pr.jus.br/legislacao/compilada/resolucoes-tre-pr/{ano}",
    "TRE-PR Instruções Normativas": "https://www.tre-pr.jus.br/legislacao/compilada/instrucoes-normativas-tre-pr/{ano}",
    "TRE-PR Normas Técnicas SECTI": "https://www.tre-pr.jus.br/legislacao/compilada/normas-tecnicas-da-secti/{ano}",
    "TRE-PR Portarias Presidência": "https://www.tre-pr.jus.br/legislacao/compilada/portarias-da-presidencia-tre-pr/{ano}",
    "TRE-PR Portarias Diretoria-Geral": "https://www.tre-pr.jus.br/legislacao/compilada/portarias-da-diretoria-geral-tre-pr/{ano}",
    "TSE Legislação": "https://www.tse.jus.br/legislacao",
    "CNJ Atos": "https://atos.cnj.jus.br/",
}

# Inventário atual do vault (para diff)
norm_dir = W / "wiki" / "normas"
catalog = sorted(p.stem for p in norm_dir.glob("*.md")) if norm_dir.exists() else []

def report():
    print("# Monitoramento normativo — estado atual")
    print(f"\nVault: {len(catalog)} páginas de normas")
    print("\nFontes oficiais monitoradas (usar extração web / navegador):")
    for name, url in SOURCES.items():
        print(f"  - {name}: {url}")

if __name__ == "__main__":
    report()
