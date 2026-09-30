from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque()

    # Initial state
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        a, b = queue.popleft()

        print("Jug 1:", a, "Jug 2:", b)

        # Check whether target is reached
        if a == target or b == target:
            print("Target reached!")
            return

        # Generate possible states
        states = [
            (jug1, b),                    # Fill Jug 1
            (a, jug2),                    # Fill Jug 2
            (0, b),                       # Empty Jug 1
            (a, 0),                       # Empty Jug 2
            (a - min(a, jug2 - b),        # Pour Jug 1 -> Jug 2
             b + min(a, jug2 - b)),
            (a + min(b, jug1 - a),        # Pour Jug 2 -> Jug 1
             b - min(b, jug1 - a))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("Target cannot be reached.")


# Example:
# Jug 1 = 4 litres
# Jug 2 = 3 litres
# Target = 2 litres

water_jug(4, 3, 2)
