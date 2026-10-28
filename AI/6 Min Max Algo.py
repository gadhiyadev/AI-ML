MAX = 1000
MIN = -1000

def minimax(depth, node_index, is_maximizing, values, alpha, beta):
    if depth == 3:
        return values[node_index]

    if is_maximizing:
        best = MIN
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best

if __name__ == "__main__":
    values = [3, 9, 1, 2, 0, -1]

    print("\n--- Minimax Algorithm with Alpha-Beta Pruning ---\n")
    print(f"Leaf Node Values: {values}")

    optimal_value = minimax(0, 0, True, values, MIN, MAX)
    print(f"The optimal value is: {optimal_value}\n")
