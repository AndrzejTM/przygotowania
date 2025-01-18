import networkx as nx
import matplotlib.pyplot as plt

def konwertuj_na_networkx(graf_obiekt):
    G = nx.DiGraph()

    for wezel in graf_obiekt.graf:
        G.add_node(str(wezel))

    for wezel, krawedzie in graf_obiekt.graf.items():
        for krawedz in krawedzie:
            if krawedz.kierunek == "N":
                G.add_edge(str(krawedz.zrodlo), str(krawedz.cel),
                           waga=krawedz.waga)
                G.add_edge(str(krawedz.cel), str(krawedz.zrodlo),
                           waga=krawedz.waga)
            else:
                G.add_edge(str(krawedz.zrodlo), str(krawedz.cel),
                           waga=krawedz.waga)

    return G


def rysuj_graf(graf_obiekt):
    G = konwertuj_na_networkx(graf_obiekt)
    pos = nx.spring_layout(G)
    nx.draw(G, pos,
            with_labels=True,
            node_size=2000,
            node_color="lightblue",
            font_size=10,
            font_weight="bold",
            arrows=True)

    edge_labels = nx.get_edge_attributes(G, 'waga')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Wizualizacja grafu")
    plt.show()
