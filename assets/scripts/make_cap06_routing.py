"""
Figuras do Cap06: encaminhamento (routing) e reencaminhamento (forwarding).

- routing-caminho.png: rede de redes; o pacote vai da rede de casa ao servidor
  da UTAD, rede a rede, e cada router escolhe a rede seguinte.
- forwarding-router.png: o que acontece dentro de um router: lê o destino,
  consulta a tabela de encaminhamento e reencaminha pela saída certa.
Largura 11in a 200dpi (2200px), letra grande, paleta do livro.
Uso: python make_cap06_routing.py   (gera PT e EN)
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

DARK = "#04170c"
GREEN = "#0e8a4d"
PALE = "#eefaf3"
GREY = "#9aa8a0"
HIGH = "#b5651d"

BIG = 22
TEXT = 18
SMALL = 16

BASE = "/Users/jpavao/QProjects/Sebenta-DAW1"
LABELS = {
    'pt': {
        'casa': 'Rede de casa', 'utad': 'Rede da UTAD', 'pc': 'PC', 'srv': 'Servidor', 'ippc': '192.168.1.10', 'ipsrv': '193.136.40.195',
        'legenda': 'R1 a R4: routers', 'router': 'router',
        'pacote': 'pacote para\n193.136.40.195', 'alt': 'caminho alternativo',
        'tabela': 'Tabela de encaminhamento do router R1', 'col1': 'Destino', 'col2': 'Sai por',
        'linhas': [("começa por 192.168.1 (casa)", "saída 1 (rede de casa)"),
                   ("começa por 193.136 (UTAD)", "saída 2 (para o router R2)"),
                   ("qualquer outro", "saída 3 (para o router R3)")],
        'saidas': ["saída 1", "saída 2", "saída 3"],
        'p1': "① lê o destino", 'p2': "② consulta a tabela", 'p3': "③ reencaminha",
        'dir': BASE + "/assets/images/cap06/",
    },
    'en': {
        'casa': 'Home network', 'utad': 'UTAD network', 'pc': 'PC', 'srv': 'Server', 'ippc': '192.168.1.10', 'ipsrv': '193.136.40.195',
        'legenda': 'R1 to R4: routers', 'router': 'router',
        'pacote': 'packet to\n193.136.40.195', 'alt': 'alternative path',
        'tabela': "Router R1's routing table", 'col1': 'Destination', 'col2': 'Leaves through',
        'linhas': [("starts with 192.168.1 (home)", "exit 1 (home network)"),
                   ("starts with 193.136 (UTAD)", "exit 2 (towards router R2)"),
                   ("any other", "exit 3 (towards router R3)")],
        'saidas': ["exit 1", "exit 2", "exit 3"],
        'p1': "① reads the destination", 'p2': "② looks up the table", 'p3': "③ forwards",
        'dir': BASE + "/en/assets/images/cap06/",
    },
}


def novo(W, H):
    fig = plt.figure(figsize=(W, H), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")
    return fig, ax


def router(ax, x, y, nome, r=0.42, cor=GREEN):
    ax.add_patch(Circle((x, y), r, facecolor=cor, edgecolor="white", linewidth=2, zorder=4))
    ax.text(x, y, nome, ha="center", va="center", fontsize=TEXT, fontweight="bold", color="white", zorder=5)


def caixa(ax, x, y, w, h, fc=PALE, ec=GREEN, lw=2, z=1):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.15",
                                facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z))


def seta(ax, a, b, cor=GREEN, lw=4, estilo="-|>", z=3, **kw):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=estilo, mutation_scale=28, color=cor, lw=lw,
                                 zorder=z, shrinkA=0, shrinkB=0, **kw))


def linha(ax, a, b, cor=GREY, lw=3, z=2, **kw):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=cor, lw=lw, zorder=z, solid_capstyle="round", **kw)


def pacote(ax, x, y, w, h, txt):
    caixa(ax, x, y, w, h, fc="white", ec=HIGH, lw=2.5, z=6)
    ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=SMALL, color=DARK,
            linespacing=1.2, zorder=7)


def fig_routing(t):
    W, H = 11.0, 5.4
    fig, ax = novo(W, H)
    # as duas redes das pontas
    caixa(ax, 0.08, 0.9, 2.3, 2.6)
    caixa(ax, 8.62, 0.9, 2.3, 2.6)
    ax.text(1.23, 3.15, t['casa'], ha="center", va="center", fontsize=TEXT, fontweight="bold", color=DARK)
    ax.text(9.77, 3.15, t['utad'], ha="center", va="center", fontsize=TEXT, fontweight="bold", color=DARK)
    caixa(ax, 0.63, 1.55, 1.2, 0.85, fc="white", ec=DARK, z=3)
    ax.text(1.23, 1.3, t['ippc'], ha="center", va="center", fontsize=SMALL, color=DARK)
    ax.text(9.77, 1.3, t['ipsrv'], ha="center", va="center", fontsize=SMALL, color=DARK)
    ax.text(10.9, 4.95, t['legenda'], ha="right", va="center", fontsize=SMALL, style="italic", color=GREEN)
    ax.text(1.23, 1.97, t['pc'], ha="center", va="center", fontsize=TEXT, fontweight="bold", color=DARK, zorder=4)
    caixa(ax, 9.07, 1.55, 1.4, 0.85, fc="white", ec=DARK, z=3)
    ax.text(9.77, 1.97, t['srv'], ha="center", va="center", fontsize=TEXT, fontweight="bold", color=DARK, zorder=4)

    R = {"R1": (3.3, 1.97), "R2": (5.5, 3.25), "R3": (5.5, 0.7), "R4": (7.7, 1.97)}
    for a, b in (("R1", "R3"), ("R3", "R4"), ("R2", "R3")):
        linha(ax, R[a], R[b])
    ax.text(5.5, 0.08, t['alt'], ha="center", va="bottom", fontsize=SMALL, style="italic", color=GREY)
    # caminho seguido pelo pacote
    pts = [(1.83, 1.97), R["R1"], R["R2"], R["R4"], (9.07, 1.97)]
    for a, b in zip(pts, pts[1:]):
        seta(ax, a, b, cor=HIGH, lw=4.5)
    for nome, (x, y) in R.items():
        router(ax, x, y, nome)
    pacote(ax, 1.3, 4.05, 3.4, 1.0, t['pacote'])
    seta(ax, (2.8, 4.05), (2.6, 2.1), cor=HIGH, lw=2, estilo="-|>", linestyle=(0, (4, 3)))
    fig.savefig(t['dir'] + "routing-caminho.png", dpi=200, facecolor="white")
    plt.close(fig)
    print(t['dir'] + "routing-caminho.png")


def fig_forwarding(t):
    W, H = 11.0, 7.0
    fig, ax = novo(W, H)
    # tabela de encaminhamento (em cima)
    tx, ty, tw, rh = 1.4, 3.7, 8.2, 0.62
    ax.text(tx + tw / 2, ty + 4 * rh + 0.3, t['tabela'], ha="center", va="center", fontsize=TEXT,
            fontweight="bold", color=DARK)
    c1 = 3.95
    for i, (a, b) in enumerate([(t['col1'], t['col2'])] + t['linhas']):
        y = ty + (3 - i) * rh
        fc = GREEN if i == 0 else ("#fbe9dc" if i == 2 else "white")
        ec = HIGH if i == 2 else GREEN
        ax.add_patch(plt.Rectangle((tx, y), tw, rh, facecolor=fc, edgecolor=GREEN, linewidth=1.5, zorder=1))
        cor = "white" if i == 0 else DARK
        peso = "bold" if i in (0, 2) else "normal"
        ax.text(tx + 0.2, y + rh / 2, a, ha="left", va="center", fontsize=SMALL, color=cor, fontweight=peso, zorder=2)
        ax.text(tx + c1 + 0.2, y + rh / 2, b, ha="left", va="center", fontsize=SMALL, color=cor, fontweight=peso, zorder=2)
        if i == 2:
            ax.add_patch(plt.Rectangle((tx, y), tw, rh, facecolor="none", edgecolor=ec, linewidth=3, zorder=3))
    ax.plot([tx + c1, tx + c1], [ty, ty + 4 * rh], color=GREEN, lw=1.5, zorder=2)

    # router e saídas (em baixo)
    rx, ry = 5.0, 1.7
    router(ax, rx, ry, "R1", r=0.7)
    ax.text(rx, ry - 0.95, t['router'], ha="center", va="center", fontsize=SMALL, style="italic", color=GREEN)
    pacote(ax, 0.05, 1.2, 3.0, 1.0, t['pacote'])
    seta(ax, (3.05, ry), (rx - 0.72, ry), cor=HIGH, lw=4.5)
    ax.text(1.55, 0.75, t['p1'], ha="center", va="center", fontsize=SMALL, fontweight="bold", color=HIGH)
    seta(ax, (rx, ry + 0.72), (rx, ty - 0.02), cor=HIGH, lw=2.5, estilo="<|-|>", linestyle=(0, (4, 3)))
    ax.text(rx + 0.2, (ry + 0.72 + ty) / 2, t['p2'], ha="left", va="center", fontsize=SMALL,
            fontweight="bold", color=HIGH)
    saidas = [(8.4, 2.9), (8.4, 1.7), (8.4, 0.5)]
    for i, ((x, y), nome) in enumerate(zip(saidas, t['saidas'])):
        a = (rx + 0.7 * (x - rx) / ((x - rx) ** 2 + (y - ry) ** 2) ** 0.5,
             ry + 0.7 * (y - ry) / ((x - rx) ** 2 + (y - ry) ** 2) ** 0.5)
        if i == 1:
            seta(ax, a, (x, y), cor=HIGH, lw=4.5)
        else:
            linha(ax, a, (x, y))
        ax.text(x + 0.15, y, nome, ha="left", va="center", fontsize=TEXT,
                fontweight="bold" if i == 1 else "normal", color=HIGH if i == 1 else GREY)
    ax.text(8.55, 1.2, t['p3'], ha="left", va="center", fontsize=SMALL, fontweight="bold", color=HIGH)
    fig.savefig(t['dir'] + "forwarding-router.png", dpi=200, facecolor="white")
    plt.close(fig)
    print(t['dir'] + "forwarding-router.png")


for lang in ('pt', 'en'):
    fig_routing(LABELS[lang])
    fig_forwarding(LABELS[lang])
