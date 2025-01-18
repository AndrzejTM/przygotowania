'''
Dane są w postaci grafu nieskierowanego ważonego w następującej postaci GRAF.
Napisz program który znajduje najkrótszą ścieżkę.
Kod powinien opierać się na budowie klasy, wraz z mechanizmami odpowiedzialnymi
za znajdowanie najkrótszej ścieżki i jej konstruowania.
'''
import heapq

class Graph:
    def __init__(self, graph_data):
        self.graph = graph_data

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        parents = {start: None}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parents[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, parents

    def shortest_path(self, start, end):
        distances, parents = self.dijkstra(start)

        if distances[end] == float('inf'):
            return None, None

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = parents[current]
        path.reverse()

        return distances[end], path

graph_wazony = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

g = Graph(graph_wazony)

distance, path = g.shortest_path('A', 'D')

if path:
    print(f"Najkrótsza ścieżka z A do D: {path} o koszcie {distance}")
else:
    print("Brak ścieżki między A i D.")
