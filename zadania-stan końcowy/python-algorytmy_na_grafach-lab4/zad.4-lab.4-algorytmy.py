import networkx as nx
import random

# Ustalamy liczbę węzłów
num_nodes = random.randint(20, 30)

# Tworzymy graf losowy (kompletny)
G = nx.erdos_renyi_graph(num_nodes, 0.5)

# Wyświetlamy liczbę węzłów i krawędzi przed awariami
initial_num_edges = G.number_of_edges()

# Funkcja do usuwania losowych krawędzi
def remove_random_edges(graph, num_to_remove):
    edges = list(graph.edges())
    edges_to_remove = random.sample(edges, num_to_remove)
    graph.remove_edges_from(edges_to_remove)

# Losujemy liczbę krawędzi do usunięcia
num_edges_to_remove = random.randint(5, 10)

# Usuwamy losowe krawędzie
remove_random_edges(G, num_edges_to_remove)

# Sprawdzamy, czy graf jest nadal spójny
is_connected = nx.is_connected(G)

# Obliczamy średnią długość najkrótszej ścieżki przed usunięciem krawędzi
G_full = nx.erdos_renyi_graph(num_nodes, 0.5)
if nx.is_connected(G_full):
    avg_shortest_path_before = nx.average_shortest_path_length(G_full)
else:
    avg_shortest_path_before = None

# Obliczamy średnią długość najkrótszej ścieżki po usunięciu krawędzi
if is_connected:
    avg_shortest_path_after = nx.average_shortest_path_length(G)
else:
    avg_shortest_path_after = None

# Wyświetlamy wyniki
print("Liczba węzłów:", num_nodes)
print("Początkowa liczba krawędzi:", initial_num_edges)
print("Usunięto krawędzi:", num_edges_to_remove)
print("Czy graf jest spójny po awariach?", is_connected)
print("Średnia długość najkrótszej ścieżki przed usunięciem krawędzi:", avg_shortest_path_before)
print("Średnia długość najkrótszej ścieżki po usunięciu krawędzi:", avg_shortest_path_after)
