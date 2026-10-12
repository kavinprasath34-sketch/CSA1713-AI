
from collections import deque

def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [])])
    visited = set()

    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    while queue:
        state, path = queue.popleft()

        if state == goal:
            for step in path + [state]:
                print(step)
            return

        if state in visited:
            continue
        visited.add(state)

        m, c, boat = state

        for dm, dc in moves:
            if boat == 0:
                new_state = (m - dm, c - dc, 1)
            else:
                new_state = (m + dm, c + dc, 0)

            nm, nc, nb = new_state

            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue

            rm, rc = 3 - nm, 3 - nc

            if ((nm > 0 and nc > nm) or
                (rm > 0 and rc > rm)):
                continue

            queue.append((new_state, path + [state]))

solve()
