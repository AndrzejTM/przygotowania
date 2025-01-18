from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    bfs_order = []

    while queue:
        node = queue.popleft()
        bfs_order.append(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

    return bfs_order

def dfs(graph, start, visited=None, dfs_order=None):
    if visited is None:
        visited = [False] * len(graph)
    if dfs_order is None:
        dfs_order = []

    visited[start] = True
    dfs_order.append(start)

    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, dfs_order)

    return dfs_order

# Lista sąsiedztwa
lista_sasiedztwa = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}

# Punkt startowy (przyjmujemy 0 jako start)
start_node = 0

# Wywołanie funkcji
bfs_result = bfs(lista_sasiedztwa, start_node)
dfs_result = dfs(lista_sasiedztwa, start_node)

# Wyniki
print("BFS order:", bfs_result)
print("DFS order:", dfs_result)
