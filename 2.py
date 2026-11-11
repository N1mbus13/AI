
g = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

def bfs(v):
    vis = set()
    q = [v]

    while q:
        x = q.pop(0)
        if x not in vis:
            print(x,end=' ')
            vis.add(x)
            q.extend(g[x])

bfs('A')
