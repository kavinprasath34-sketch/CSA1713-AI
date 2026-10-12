
from itertools import permutations

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)
min_cost = float('inf')
best_path = []

for path in permutations(range(1, n)):
    route = (0,) + path + (0,)
    cost = 0

    for i in range(len(route) - 1):
        cost += dist[route[i]][route[i + 1]]

    if cost < min_cost:
        min_cost = cost
        best_path = route

print("Best Path:", best_path)
print("Minimum Cost:", min_cost)
