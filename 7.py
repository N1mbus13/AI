def minimax(depth, index, maximizing, scores, alpha, beta, max_depth):
    if depth == max_depth:
        return scores[index]

    if maximizing:
        best = float('-inf')
        for i in range(2):
            val = minimax(depth + 1, index * 2 + i, False,
                          scores, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth + 1, index * 2 + i, True,
                          scores, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


scores = [3, 5, 6, 9, 1, 2, 0, -1]
depth = 3

result = minimax(0, 0, True, scores, float('-inf'), float('inf'), depth)

print("Leaf nodes:", scores)
print("Optimal value:", result)