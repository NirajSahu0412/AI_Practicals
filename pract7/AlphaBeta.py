MAX, MIN = 1000, -1000


def minimax(depth, nodeIndex, alpha, beta, maximizingPlayer, values):
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = MIN
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, alpha, beta, False, values)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, alpha, beta, True, values)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


values = [3, 15, 6, 9, 1, 2, 0, -1]
print("The Best value is:", minimax(0, 0, MIN, MAX, True, values))

# Output: The Best value is: 9
