#BFS implementation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(start):
    visited = {start}
    queue = [start]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)

bfs('A')