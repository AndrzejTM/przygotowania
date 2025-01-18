from heapq import heappop, heappush


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def find_shortest_path(self, start_node, end_node):
        distances = {node: float('inf') for node in self.graph}
        distances[start_node] = 0

        pq = [(0, start_node)]  # (odległość, wierzchołek)

        predecessors = {node: None for node in self.graph}

        while pq:
            current_distance, current_node = heappop(pq)

            if current_node == end_node:
                break

            for neighbor, weight in self.graph[current_node].items():
                temp_distance = current_distance + weight

                if temp_distance < distances[neighbor]:
                    distances[neighbor] = temp_distance
                    predecessors[neighbor] = current_node
                    heappush(pq, (temp_distance, neighbor))

        path = []
        current_node = end_node

        while current_node is not None:
            path.append(current_node)
            current_node = predecessors[current_node]

        path.reverse()

        return path, distances[end_node]


if __name__ == "__main__":
    graf_wazony = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    dijkstra_solver = Dijkstra(graf_wazony)

    path, distance = dijkstra_solver.find_shortest_path('A', 'D')
    print("Najkrótsza ścieżka:", path)
    print("Długość najkrótszej ścieżki:", distance)
