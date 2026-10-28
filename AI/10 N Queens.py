def is_safe(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def solve_n_queens(n):
    solutions = []

    def backtrack(row, current_board):
        if row == n:
            solutions.append(list(current_board))
            return

        for col in range(1, n + 1):
            if is_safe(current_board, row, col):
                current_board.append(col)
                backtrack(row + 1, current_board)
                current_board.pop()

    backtrack(0, [])
    return solutions

def print_board(solution):
    n = len(solution)
    for col in solution:
        row_str = [" . "] * n
        row_str[col - 1] = " Q "
        print("".join(row_str))
    print()

if __name__ == "__main__":
    n = 4
    print(f"\n--- Solving {n}-Queens Problem ---\n")
    solutions = solve_n_queens(n)

    print(f"Total solutions found: {len(solutions)}\n")
    for i, sol in enumerate(solutions, 1):
        print(f"Solution {i}: {sol}")
        print_board(sol)
