def minimax(depth, node_index, is_max, scores, target_depth):
    """
    depth: current depth in tree
    node_index: index of current node
    is_max: True if it's maximizer's turn
    scores: list of leaf node values
    target_depth: depth of leaf nodes
    """

    # If leaf node is reached, return score
    if depth == target_depth:
        return scores[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, target_depth),
            minimax(depth + 1, node_index * 2 + 1, False, scores, target_depth)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, target_depth),
            minimax(depth + 1, node_index * 2 + 1, True, scores, target_depth)
        )


# Example game tree
scores = [3, 5, 2, 9, 12, 5, 23, 23]

# Tree depth = 3
tree_depth = 3

best_score = minimax(0, 0, True, scores, tree_depth)

print("The optimal value is:", best_score)