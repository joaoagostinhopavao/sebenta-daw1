# Sebenta DAW1 — Desenvolvimento de Aplicações Web I

Projecto Quarto para a sebenta da UC de Desenvolvimento de Aplicações Web I,
Licenciatura em Comunicação e Multimédia, UTAD.

## Estrutura

```
Sebenta-DAW1/
├── _quarto.yml          # Configuração do projecto
├── index.qmd             # Prefácio
├── capitulos/
│   ├── cap01.qmd         # Desenvolvimento de Software para o Ambiente Web
│   ├── cap02.qmd         # Arquiteturas Web e Infraestruturas
│   └── ...                # Capítulos seguintes
├── assets/
│   ├── css/custom.css    # Estilos personalizados
│   ├── images/           # Imagens e figuras (uma pasta por capítulo)
│   └── cover.tex          # Capa PDF (TikZ)
└── referencias.bib        # Bibliografia
```

## Renderização

```bash
# HTML interativo
quarto render --to html

# PDF via LuaLaTeX
quarto render --to pdf

# Preview com hot reload
quarto preview
```

## Estado

Projecto criado em 2026-08-22. Estrutura dos 11 capítulos definida a partir
do planeamento em `Planeamento de UUCC/DAW1/Planeamento DAW1.canvas`.
Capítulos ainda por escrever.

## Autor

João Pavão — UTAD, 2026 (componente teórica, autor dos capítulos)
