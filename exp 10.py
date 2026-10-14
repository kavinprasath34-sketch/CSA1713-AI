
def astar(graph, heuristic, start, goal):
    open_list = [(heuristic[start], 0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            return path, g

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                open_list.append(
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, -1


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'E': 1},
    'D': {'E': 1},
    'E': {}
}

heuristic = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'E': 0
}

path, cost = astar(graph, heuristic, 'A', 'E')

print("Shortest Path:", path)
print("Total Cost:", cost)
