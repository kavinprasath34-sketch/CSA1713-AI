graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

heuristic = {
    'A': 7, 'B': 5, 'C': 2, 'D': 6,
    'E': 4, 'F': 1, 'G': 0, 'H': 3, 'I': 5
}

def beam_search(start, width):
    beam = [start]

    while beam:
        print("Beam:", beam)

        if 'G' in beam:
            print("Goal Found: G")
            return

        children = []

        for node in beam:
            children.extend(graph[node])

        beam = sorted(children, key=lambda x: heuristic[x])[:width]

    print("Goal not found")


beam_search('A', 2)
