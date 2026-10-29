"""
Figura do Cap06: as camadas no envio de uma carta da Rita ao Tiago.

Mesma figura do slide "Exemplo: as Camadas no Envio de uma Carta" do deck
da Aula 7, redesenhada com a paleta do livro. A camada de baixo chama-se
"Circulação" (e não "Transporte", para não colidir com a camada de transporte).
Largura 11in a 200dpi (2200px), letra grande, como nas outras figuras.
Uso: python make_cap06_carta.py   (gera PT e EN)
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

DARK = "#04170c"
GREEN = "#0e8a4d"
PALE = "#eefaf3"
PEER = "#b5651d"

NAME = 22
TEXT = 17
HEAD = 18

BASE = "/Users/jpavao/QProjects/Sebenta-DAW1"
LABELS = {
    'pt': {
        'envio': 'ENVIO (desce)', 'rececao': 'RECEÇÃO (sobe)',
        'esq': [("Rita", "escreve a carta"),
                ("Secretária", "envelope, morada e\ncorreio registado"),
                ("Correios", "escolhem o caminho\npelo código postal")],
        'dir': [("Tiago", "lê a carta"),
                ("Secretária", "assina o aviso\nde receção"),
                ("Correios", "entregam na morada")],
        'pares': ["a mesma língua", "aviso de receção", "códigos postais"],
        'base': ("Circulação", "carrinha, comboio ou avião"),
        'out': BASE + "/assets/images/cap06/carta-camadas.png",
    },
    'en': {
        'envio': 'SENDING (down)', 'rececao': 'RECEIVING (up)',
        'esq': [("Rita", "writes the letter"),
                ("Secretary", "envelope, address and\nregistered post"),
                ("Post office", "chooses the route\nby postcode")],
        'dir': [("Tiago", "reads the letter"),
                ("Secretary", "signs the proof\nof delivery"),
                ("Post office", "delivers to the address")],
        'pares': ["the same language", "proof of delivery", "postcodes"],
        'base': ("Circulation", "van, train or plane"),
        'out': BASE + "/en/assets/images/cap06/carta-camadas.png",
    },
}


def draw(t):
    W, H = 11.0, 7.4
    fig = plt.figure(figsize=(W, H), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    bw, bh, gap = 3.7, 1.38, 0.5
    xl, xr = 0.08, W - 0.08 - bw
    ty, th = 0.08, 1.0
    topo = H - 0.62
    linhas = [topo - bh - i * (bh + gap) for i in range(3)]

    def caixa(x, y, w, h, nome, txt):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.12",
                                    facecolor=PALE, edgecolor=GREEN, linewidth=2, zorder=2))
        ax.text(x + w / 2, y + h - 0.34, nome, ha="center", va="center", fontsize=NAME,
                fontweight="bold", color=DARK, zorder=3)
        ax.text(x + w / 2, y + h - 0.66, txt, ha="center", va="top", fontsize=TEXT,
                color=DARK, linespacing=1.15, zorder=3)

    def seta(x0, y0, x1, y1, cor=DARK, lw=3, estilo="-|>", **kw):
        ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=estilo, mutation_scale=26,
                                     color=cor, lw=lw, zorder=1, shrinkA=0, shrinkB=0, **kw))

    ax.text(xl + bw / 2, H - 0.4, t['envio'], ha="center", va="baseline", fontsize=HEAD,
            fontweight="bold", color=GREEN)
    ax.text(xr + bw / 2, H - 0.4, t['rececao'], ha="center", va="baseline", fontsize=HEAD,
            fontweight="bold", color=GREEN)

    for y, (n1, t1), (n2, t2), p in zip(linhas, t['esq'], t['dir'], t['pares']):
        caixa(xl, y, bw, bh, n1, t1)
        caixa(xr, y, bw, bh, n2, t2)
        ym = y + bh / 2
        seta(xl + bw + 0.12, ym, xr - 0.12, ym, cor=PEER, lw=2.4, estilo="<|-|>",
             linestyle=(0, (5, 4)))
        ax.text(W / 2, ym + 0.14, p, ha="center", va="bottom", fontsize=TEXT, style="italic",
                color=PEER)

    # setas verticais: desce do lado da Rita, sobe do lado do Tiago
    alvos = [y + bh for y in linhas[1:]] + [ty + th]
    for a, b in zip(linhas, alvos):
        seta(xl + bw / 2, a, xl + bw / 2, b)
        seta(xr + bw / 2, b, xr + bw / 2, a)

    # circulação, partilhada pelos dois lados
    nome, txt = t['base']
    ax.add_patch(FancyBboxPatch((xl, ty), W - 2 * xl, th, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=PALE, edgecolor=GREEN, linewidth=2, zorder=2))
    ax.text(W / 2, ty + th - 0.32, nome, ha="center", va="center", fontsize=NAME,
            fontweight="bold", color=DARK, zorder=3)
    ax.text(W / 2, ty + 0.28, txt, ha="center", va="center", fontsize=TEXT, color=DARK, zorder=3)

    fig.savefig(t['out'], dpi=200, facecolor="white")
    plt.close(fig)
    print(t['out'])


for lang in ('pt', 'en'):
    draw(LABELS[lang])
