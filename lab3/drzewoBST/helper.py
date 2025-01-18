import matplotlib.pyplot as plt
import networkx as nx


def _rysuj_drzewo(wezel, graf, pozycje,
                  poziom=0,
                  poziom_y=1,
                  poziom_x=0.5,
                  x_shift=1):
    if wezel is not None:
        if wezel.lewy:
            graf.add_edge(wezel.klucz, wezel.lewy.klucz)
            pozycje[wezel.lewy.klucz] = (poziom_x - x_shift,
                                         poziom_y - poziom - 1)
            _rysuj_drzewo(wezel.lewy, graf, pozycje, poziom + 1,
                          poziom_y, poziom_x - x_shift, x_shift / 2)
        if wezel.prawy:
            graf.add_edge(wezel.klucz, wezel.prawy.klucz)
            pozycje[wezel.prawy.klucz] = (poziom_x + x_shift,
                                          poziom_y - poziom - 1)
            _rysuj_drzewo(wezel.prawy, graf, pozycje, poziom + 1,
                          poziom_y, poziom_x + x_shift, x_shift / 2)


def wizualizuj_drzewo(korzen):
    if korzen is None:
        print("Drzewo jest puste")
        return

    graf = nx.DiGraph()
    pozycje = {korzen.klucz: (0, 0)}
    _rysuj_drzewo(korzen, graf, pozycje)

    plt.figure(figsize=(8, 6))
    nx.draw(graf, pos=pozycje, with_labels=True, node_size=5000,
            node_color="skyblue", font_size=10, font_weight="bold",
            arrows=False)
    plt.show()
