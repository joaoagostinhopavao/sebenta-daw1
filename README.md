# Sebenta DAW1 — Desenvolvimento de Aplicações Web I

Projecto Quarto para a sebenta da UC de Desenvolvimento de Aplicações Web I,
Licenciatura em Comunicação e Multimédia, UTAD.

## Estrutura

```
Sebenta-DAW1/
├── _quarto.yml          # Configuração do projecto (PT)
├── index.qmd             # Prefácio
├── capitulos/
│   ├── cap01.qmd         # Desenvolvimento de Software para o Ambiente Web
│   ├── cap02.qmd         # Arquiteturas Web e Infraestruturas
│   ├── ...                # cap03.qmd … cap11.qmd
│   ├── apendiceA.qmd     # Configuração do Ambiente de Desenvolvimento
│   ├── apendiceB.qmd     # Demos de Código das Aulas
│   ├── apendiceC.qmd     # Desafios de Programação
│   ├── apendiceD.qmd     # Complementos de Redes de Computadores
│   └── apendiceE.qmd     # Complementos sobre o HTTP
├── assets/
│   ├── css/custom.css    # Estilos personalizados
│   ├── images/           # Imagens e figuras (uma pasta por capítulo, heroes/, capa/)
│   └── cover.tex          # Capa PDF (TikZ; a imagem em si vem de assets/images/capa/PDF/)
├── en/                    # Versão em inglês (projecto Quarto próprio, HTML + PDF)
│   ├── _quarto.yml
│   ├── index.qmd
│   ├── capitulos/         # cap01.qmd … cap11.qmd + apendiceA.qmd … apendiceE.qmd, em inglês (completo)
│   └── assets/
│       ├── cover.tex          # Cópia própria (ver nota abaixo — capa reutiliza a imagem PT)
│       ├── css/custom.css     # Cópia própria (ver nota abaixo)
│       └── images/            # Cópia própria de heroes/, cap06/ e capa/ (ver nota abaixo)
└── referencias.bib        # Bibliografia
```

## Renderização

```bash
# Versão portuguesa — livro completo (HTML + PDF)
quarto render

# Versão inglesa — HTML + PDF
quarto render en/

# Preview com hot reload (cada versão tem de ser aberta em separado)
quarto preview
quarto preview en/
```

A versão em inglês (`en/`) segue o mesmo padrão já usado nas outras sebentas
bilingues deste autor (Sebenta-ASW, Sebenta-IM): projecto Quarto irmão, com
`output-dir: ../docs/en`, gerando o site em `docs/en/`. O botão de mudança
de idioma fica na barra lateral, ao lado do toggle claro/escuro
(`book.sidebar.tools`), em ambas as versões.

**Nota sobre o CSS e as imagens da versão inglesa:** os caminhos
`assets/css/custom.css` e `../assets/images/...` usados em `en/` resolvem-se
à raiz do *site* do próprio subprojecto `en/` (`docs/en/`), não à pasta
principal (`docs/`). Por isso existem cópias próprias em
`en/assets/css/custom.css` e `en/assets/images/` — sempre que o CSS
principal ou uma imagem forem alterados na pasta principal, replicar
também aqui.

**Nota sobre a capa da versão inglesa:** ao contrário da Sebenta-ASW e da
Sebenta-IM (onde a capa é gerada em TikZ, com o título como texto — fácil
de traduzir), a capa desta sebenta é uma imagem única já desenhada
(`assets/images/capa/PDF/capa-4-5.jpg`), com o título em português
desenhado na própria imagem. A versão inglesa **reutiliza esta mesma
imagem por agora** — não foi criada uma capa alternativa em inglês, por
não haver uma fonte editável (Canva/Illustrator) para lhe alterar só o
texto. Se for necessária uma capa em inglês genuína, terá de se desenhar
de raiz uma nova imagem (ou recriar a capa em TikZ, ao estilo das outras
duas sebentas).

**Nota sobre o exemplo "Revista Contraponto":** os capítulos de PHP (3-8) e
os Apêndices B, C e E partilham um exemplo narrativo contínuo (o projeto
da revista fictícia Contraponto, personagens Rita Ferreira e Tiago
Correia). Na versão inglesa, todo o código PHP deste exemplo (nomes de
variáveis, chaves de array, valores de exemplo) foi mantido **em
português, sem tradução** — só a prosa e os comentários de código foram
traduzidos. Esta foi uma decisão editorial deliberada: como o mesmo
exemplo atravessa múltiplos capítulos, traduzir os identificadores exigiria
uma única passagem coordenada sobre o livro inteiro (não um capítulo de
cada vez), para garantir que `$titulos`/`$artigo`/`"categoria"` (ou os
seus equivalentes) permanecem exactamente iguais em todo o lado onde o
exemplo é reutilizado.

## Estado

Projecto criado em 2026-08-22. **Todos os 11 capítulos e os 5 apêndices têm
conteúdo real, em português e em inglês.** Estrutura definida a partir do
planeamento em `Planeamento de UUCC/DAW1/Planeamento DAW1.canvas`.

## Autor

João Pavão — UTAD, 2026 (componente teórica, autor dos capítulos)
