def safe(g, col, n, c):
    return all(col[x] != c for x in g[n])

def color_graph(g, colors, col, n=0):
    if n == len(g):
        return True 
    for c in colors:
        if safe(g, col, n, c):
            col[n] = c
            if color_graph(g, colors, col, n+1):
                return True
            col[n] = None
    return False

g = {0:[1,2], 1:[0,2,3], 2:[0,1,3], 3:[1,2]}
colors = ["Red", "Green", "Blue"]
col = [None] * len(g)

if color_graph(g, colors, col):
    print("Solution exists with coloring:")
    for n in range(len(g)):
        print(f"Node {n} --> {col[n]}")
else:
    print("No solution exists")