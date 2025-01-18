from heapq import heapify, heappop, heappush

def dijkstra(graf, start_node):

    distances = {node: float('inf') for node in graf}
    distances[start_node] = 0


    pq = [(0, start_node)]
    heapify(pq)

    visited = set()

    while pq:
        current_distance, current_node = heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graf[current_node].items():
            temp_distance = current_distance + weight

            if temp_distance < distances[neighbor]:

                distances[neighbor] = temp_distance

                heappush(pq, (temp_distance, neighbor))

    return distances

graf_wazony = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}


startowy_wierzcholek = 'A'
wynik = dijkstra(graf_wazony, startowy_wierzcholek)

print(f"Najkrótsze odległości od wierzchołka '{startowy_wierzcholek}':")
for wierzcholek, odleglosc in wynik.items():
    print(f"{wierzcholek}: {odleglosc}")
