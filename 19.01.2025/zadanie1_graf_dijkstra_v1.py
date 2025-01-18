'''
Dane są w postaci grafu nieskierowanego ważonego w następującej postaci GRAF.
Napisz program który znajduje najkrótszą ścieżkę.
Kod powinien opierać się na budowie klasy, wraz z mechanizmami odpowiedzialnymi
za znajdowanie najkrótszej ścieżki i jej konstruowania.
'''
import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        parents = {start: None}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parents[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, parents

    def shortest_path(self, start, end):
        distances, parents = self.dijkstra(start)

        if distances[end] == float('inf'):
            return None, None  # Brak ścieżki

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = parents[current]
        path.reverse()

        return distances[end], path

g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 8)
g.add_edge('C', 'E', 10)
g.add_edge('D', 'E', 2)
g.add_edge('D', 'Z', 6)
g.add_edge('E', 'Z', 3)

distance, path = g.shortest_path('A', 'Z')

if path:
    print(f"Najkrótsza ścieżka z A do Z: {path} o koszcie {distance}")
else:
    print("Brak ścieżki między A i Z.")
