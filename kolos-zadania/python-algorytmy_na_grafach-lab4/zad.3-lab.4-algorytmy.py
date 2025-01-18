import networkx as nx
import random

# Tworzenie grafu skierowanego
G = nx.DiGraph()

# Dodawanie węzłów
wezly = ["A", "B", "C", "D", "E", "F", "G"]
G.add_nodes_from(wezly)

# Dodawanie losowych krawędzi z wagami
random.seed(42)  # Dla powtarzalności wyników
for _ in range(10):
    od_wezla = random.choice(wezly)
    do_wezla = random.choice(wezly)
    if od_wezla != do_wezla:
        przepustowosc = random.randint(5, 20)
        G.add_edge(od_wezla, do_wezla, capacity=przepustowosc)

# Definicja źródła i ujścia
zrodlo = "A"
ujscie = "G"

# Obliczanie maksymalnego przepływu
flow_value, flow_dict = nx.maximum_flow(G, zrodlo, ujscie)

# Wyświetlenie wyników
print(f"Maksymalny przepływ z {zrodlo} do {ujscie}: {flow_value}")
print("Przepływ na krawędziach:")
for od_wezla, przeplywy in flow_dict.items():
    for do_wezla, przeplyw in przeplywy.items():
        if przeplyw > 0:
            print(f"{od_wezla} -> {do_wezla}: {przeplyw} / {G[od_wezla][do_wezla]['capacity']}")

# Wyświetlenie krawędzi o największej przepustowości w maksymalnym przepływie
najwieksze_przeplywy = []
for od_wezla, przeplywy in flow_dict.items():
    for do_wezla, przeplyw in przeplywy.items():
        if przeplyw > 0:
            najwieksze_przeplywy.append((od_wezla, do_wezla, przeplyw))

najwieksze_przeplywy.sort(key=lambda x: x[2], reverse=True)
print("\nKrawędzie o największej przepustowości w maksymalnym przepływie:")
for od_wezla, do_wezla, przeplyw in najwieksze_przeplywy[:3]:
    print(f"{od_wezla} -> {do_wezla}: {przeplyw}")
