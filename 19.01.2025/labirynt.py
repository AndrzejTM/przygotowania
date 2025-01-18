def dfs_maze_recursive(maze, current, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    x, y = current
    if current == end:
        # Zwróć finalną ścieżkę, gdy osiągnięto cel
        return path + [current]

    # Dodaj obecny węzeł jako odwiedzony
    visited.add(current)
    path.append(current)

    rows, cols = len(maze), len(maze[0])
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Ruch w górę, dół, lewo, prawo
        nx, ny = x + dx, y + dy
        # Sprawdź, czy następne pole jest poprawne (brak ściany i węzeł nieodwiedzony)
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
            # Wywołaj rekurencyjnie funkcję dla następnego pola
            result = dfs_maze_recursive(maze, (nx, ny), end, visited, path)
            if result:
                return result

    # Cofnij się (usuń ostatni węzeł z path, jeśli nie ma dalszej drogi)
    path.pop()
    return None

# Labirynt (0 = ścieżka, 1 = ściana)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Zdefiniuj początek i koniec (współrzędne: wiersz, kolumna)
start = (0, 0)
end = (4, 4)

# Wywołaj funkcję
path = dfs_maze_recursive(maze, start, end)

print("Path in maze:", path)