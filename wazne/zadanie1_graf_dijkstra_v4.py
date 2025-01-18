from heapq import heappop, heappush


class Graph:
    def __init__(self):
       self.graph = {}

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        if node2 not in self.graph:
            self.graph[node2] = {}
        self.graph[node1][node2] = weight
        self.graph[node2][node1] = weight

    def dijkstra(self, start_node):
        distances = {node: float('inf') for node in self.graph}
        distances[start_node] = 0

        pq = [(0, start_node)]  # (odległość, wierzchołek)

        predecessors = {node: None for node in self.graph}

        while pq:
            current_distance, current_node = heappop(pq)

            for neighbor, weight in self.graph[current_node].items():
                temp_distance = current_distance + weight
                if temp_distance < distances[neighbor]:
                    distances[neighbor] = temp_distance
                    predecessors[neighbor] = current_node
                    heappush(pq, (temp_distance, neighbor))

        return distances, predecessors

    def shortest_path(self, start_node, end_node):
        distances, predecessors = self.dijkstra(start_node)

        path = []
        current_node = end_node

        while current_node is not None:
            path.append(current_node)
            current_node = predecessors[current_node]

        path.reverse()

        return path, distances[end_node]


if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    path, distance = g.shortest_path('A', 'D')
    print("Najkrótsza ścieżka:", path)
    print("Długość najkrótszej ścieżki:", distance)
