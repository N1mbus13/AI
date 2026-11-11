
import heapq

g = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['G'],
    'D':[],
    'E':['F'],
    'F':[],
    'G':[]
}

h = {'A':5,'B':3,'C':2,'D':6,'E':1,'F':0,'G':4}

def best(v,goal):
    vis = set()
    q = [(h[v],v)]

    while q:
        _,x = heapq.heappop(q)
        print("Visiting:",x)

        if x == goal:
            print("Goal reached!")
            return

        if x not in vis:
            vis.add(x)
            for n in g[x]:
                heapq.heappush(q,(h[n],n))

best('A','F')
