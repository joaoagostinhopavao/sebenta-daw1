"""
Figura 2.1: percurso de um pedido a uma página dinâmica PHP
(cliente -> Apache -> PHP -> MySQL -> PHP -> Apache -> cliente).

Segue a disposição do slide "Cliente-servidor no contexto PHP" do deck
DAW-I-2025 (frontend à esquerda, backend à direita, HTTP ao meio).
Largura 11in a 200dpi (2200px), letra grande, como nas outras sebentas.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse, Rectangle

DARK = "#04170c"
GREEN = "#0e8a4d"
LIGHT = "#4be08a"
PALE = "#eefaf3"
GREY = "#5a6b60"

TITLE = 24
BOX = 21
LABEL = 18

LABELS = {'pt': {'cli': 'Cliente\n(frontend)', 'srv': 'Servidor\n(backend)', 'l1': '1. pedido\nartigos.php?id=5', 'l6': '6. resposta\n(HTML)', 'l5': '5. HTML', 'l3': '3. SQL', 'l4': '4. dados', 'out': '/Users/jpavao/QProjects/Sebenta-DAW1/assets/images/cap02/pedido-dinamico.png'}, 'en': {'cli': 'Client\n(frontend)', 'srv': 'Server\n(backend)', 'l1': '1. request\nartigos.php?id=5', 'l6': '6. response\n(HTML)', 'l5': '5. HTML', 'l3': '3. SQL', 'l4': '4. data', 'out': '/Users/jpavao/QProjects/Sebenta-DAW1/en/assets/images/cap02/pedido-dinamico.png'}}


def draw(t):
    W, H = 11.0, 6.4
    fig = plt.figure(figsize=(W, H), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")


    def region(x0, x1, title):
        ax.add_patch(FancyBboxPatch((x0, 0.25), x1 - x0, H - 0.5,
                                    boxstyle="round,pad=0,rounding_size=0.15",
                                    facecolor=PALE, edgecolor=GREEN, linewidth=2))
        ax.text((x0 + x1) / 2, H - 0.6, title, ha="center", va="center",
                fontsize=TITLE, fontweight="bold", color=DARK)


    def box(x0, y0, w, h, text):
        ax.add_patch(FancyBboxPatch((x0, y0), w, h,
                                    boxstyle="round,pad=0,rounding_size=0.12",
                                    facecolor=GREEN, edgecolor="white", linewidth=2))
        ax.text(x0 + w / 2, y0 + h / 2, text, ha="center", va="center",
                fontsize=BOX, fontweight="bold", color="white", linespacing=1.15)


    def cylinder(x0, y0, w, h, text):
        e = 0.35
        ax.add_patch(Rectangle((x0, y0), w, h, facecolor=DARK, edgecolor="none"))
        ax.add_patch(Ellipse((x0 + w / 2, y0), w, e, facecolor=DARK, edgecolor="none"))
        ax.add_patch(Ellipse((x0 + w / 2, y0 + h), w, e, facecolor=GREEN,
                             edgecolor="white", linewidth=2))
        ax.text(x0 + w / 2, y0 + h / 2 - 0.05, text, ha="center", va="center",
                fontsize=BOX, fontweight="bold", color="white")


    def arrow(p, q, color=DARK):
        ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=28,
                                     color=color, linewidth=3, zorder=5))


    def label(x, y, text, ha="center"):
        ax.text(x, y, text, ha=ha, va="center", fontsize=LABEL, color=DARK,
                linespacing=1.15, zorder=6)


    region(0.2, 3.0, t["cli"])
    region(5.6, 10.8, t["srv"])

    box(0.5, 2.55, 2.2, 1.3, "Browser")
    box(6.0, 3.35, 2.1, 1.1, "Apache")
    box(6.0, 0.8, 2.1, 1.1, "PHP")
    cylinder(8.95, 0.75, 1.55, 1.25, "MySQL")

    # 1 e 6: HTTP entre browser e Apache
    arrow((2.7, 3.6), (6.0, 4.2))
    label(4.3, 4.6, t["l1"])
    arrow((6.0, 3.55), (2.7, 2.8), color=GREEN)
    label(4.3, 2.5, t["l6"])

    # 2 e 5: Apache <-> PHP
    arrow((6.5, 3.35), (6.5, 1.9))
    label(6.3, 2.62, "2", ha="right")
    arrow((7.6, 1.9), (7.6, 3.35), color=GREEN)
    label(7.75, 2.95, t["l5"], ha="left")

    # 3 e 4: PHP <-> MySQL
    arrow((8.1, 1.65), (8.95, 1.65))
    label(8.52, 2.15, t["l3"])
    arrow((8.95, 1.0), (8.1, 1.0), color=GREEN)
    label(8.52, 0.5, t["l4"])

    fig.savefig(t["out"], facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    import os
    from PIL import Image
    for t in LABELS.values():
        os.makedirs(os.path.dirname(t["out"]), exist_ok=True)
        draw(t)
        print(t["out"], Image.open(t["out"]).size)
