import heapq

def best_first_search(graph, start, goal, h):
    visited = set()
    pq = [(h[start], start)]

    while pq:
        h_value, node = heapq.heappop(pq)
        print(node, end=" ")

        if node == goal:
            print("\nGoal reached!")
            return

        visited.add(node)

        for n in graph[node]:
            if n not in visited:
                heapq.heappush(pq, (h[n], n))

    print("\nGoal not found!")

graph = {
    'A':['B','C'], 
    'B':['D','E'], 
    'C':['F'],
    'D':[], 
    'E':['F'], 
    'F':[]
}

h = {'A':6, 
     'B':5, 
     'C':3, 
     'D':4, 
     'E':1, 
     'F':0
    }

best_first_search(graph, 'A', 'F', h)

