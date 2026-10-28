def dfs_water_jug(c1, c2, target):
    start_state = (0, 0)
    stack = [(start_state, [("Initial State", start_state)])]
    visited = set()

    while stack:
        (x, y), path = stack.pop()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        if x == target or y == target:
            return path

        pour1_to_2 = min(x, c2 - y) 
        pour2_to_1 = min(y, c1 - x) 
        operations = [
            (f"Fill Jug 1 ({c1}L)", (c1, y)),
            (f"Fill Jug 2 ({c2}L)", (x, c2)),
            ("Empty Jug 1", (0, y)),
            ("Empty Jug 2", (x, 0)),
            ("Pour Jug 1 -> Jug 2", (x - pour1_to_2, y + pour1_to_2)),
            ("Pour Jug 2 -> Jug 1", (x + pour2_to_1, y - pour2_to_1)),
        ]

        for action_name, next_state in reversed(operations):
            if next_state not in visited:
                stack.append((next_state, path + [(action_name, next_state)]))

    return None

if __name__ == "__main__":
    jug1_cap = 4
    jug2_cap = 3
    target = 2

    print("=" * 48)
    print(f"  DFS WATER JUG PROBLEM (Target: {target}L)")
    print(f"  Capacities -> Jug 1: {jug1_cap}L | Jug 2: {jug2_cap}L")
    print("=" * 48)

    solution = dfs_water_jug(jug1_cap, jug2_cap, target)

    if solution:
        print(f"\nSolution found in {len(solution) - 1} steps:\n")
        print(f"{'Step':<6} | {'Action':<22} | {'(Jug 1, Jug 2)':<15}")
        print("-" * 48)
        for step, (action, state) in enumerate(solution):
            print(f"{step:<6} | {action:<22} | {str(state):<15}")
        print("\n")
    else:
        print("\nNo solution possible for the given configuration.")
