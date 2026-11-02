import heapq

def astar(graph, start, goal, h):
    pq = [(h[start], 0, start, [])]
    visited = set()

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)
        path = path + [node]

        if node == goal:
            return path, cost

        for next, c in graph[node]:
            new_cost = cost + c
            heapq.heappush(pq, (new_cost + h[next], new_cost, next, path))

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': [('E', 2)],
    'E': []
}

h = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0}

path, cost = astar(graph, 'A', 'E', h)
print("Path:", path)
print("Cost:", cost)