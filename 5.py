import heapq

g = {
    'A':{'B':2,'C':5},
    'B':{'D':4,'E':2},
    'C':{'H':2},
    'D':{'G':3},
    'E':{'G':2,'H':3},
    'H':{'G':1},
    'G':{}
}

h = {'A':6,'B':4,'C':4,'D':3,'E':2,'H':1,'G':0}

def astar(start,goal):
    q = [(h[start],start,0,[start])]
    vis = set()

    while q:
        f,v,cost,path = heapq.heappop(q)

        if v == goal:
            return path,cost

        if v not in vis:
            vis.add(v)
            for n,w in g[v].items():
                if n not in vis:
                    new = cost + w
                    heapq.heappush(q,(new+h[n],n,new,path+[n]))

path,cost = astar('A','G')
print("Path:",path)
print("Cost:",cost)
