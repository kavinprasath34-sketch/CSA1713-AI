# 8-Puzzle Problem using A* Search

from heapq import heappush, heappop

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Possible moves of blank space
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def heuristic(state):
    """Calculate Manhattan distance."""
    distance = 0

    for i in range(9):
        if state[i] == 0:
            continue

        goal_pos = goal.index(state[i])

        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(goal_pos, 3)

        distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


def get_neighbors(state):
    """Generate possible next states."""
    neighbors = []

    zero = state.index(0)
    x, y = divmod(zero, 3)

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_pos = nx * 3 + ny

            new_state = list(state)
            new_state[zero], new_state[new_pos] = \
                new_state[new_pos], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def solve(start):
    priority_queue = []
    heappush(priority_queue, (heuristic(start), 0, start, []))

    visited = set()

    while priority_queue:
        f, cost, state, path = heappop(priority_queue)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path + [state]

        for next_state in get_neighbors(state):
            if next_state not in visited:
                new_cost = cost + 1
                new_path = path + [state]

                heappush(
                    priority_queue,
                    (new_cost + heuristic(next_state),
                     new_cost,
                     next_state,
                     new_path)
                )

    return None


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()


# Initial state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

solution = solve(start)

if solution:
    print("Solution found:")
    for step in solution:
        print_state(step)
else:
    print("No solution exists.")
