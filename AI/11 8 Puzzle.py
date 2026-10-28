def print_board(state):
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()

def get_next_states(state):
    next_states = []
    zero_pos = state.index(0)
    row = zero_pos // 3
    col = zero_pos % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
            next_states.append(tuple(new_state))

    return next_states

def solve_puzzle(start, goal):
    queue = [(start, [start])]
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.pop(0)

        if current == goal:
            return path

        for nxt in get_next_states(current):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))

    return None

if __name__ == "__main__":
    start = (1, 2, 3, 0, 4, 6, 7, 5, 8)
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    print("\nInitial state:")
    print_board(start)

    print("Goal state:")
    print_board(goal)

    solution = solve_puzzle(start, goal)

    if solution:
        print("Solution steps:")
        for step in solution:
            print_board(step)
    else:
        print("No solution found.")
