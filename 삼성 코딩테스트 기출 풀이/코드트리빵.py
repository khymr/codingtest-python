import sys
input = sys.stdin.readline
import copy
INF = int(1e9)
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def find_camp(graph):
    basecamp = []
    for i in range(n):
        for j in range(n):
            if(graph[i][j] == 1):
                basecamp.append((i,j))
    return basecamp
                
n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
basecamp = find_camp(graph)
target = []
people = []
for _ in range(m):
    a,b = map(int, input().split())
    target.append((a-1, b-1))
idx = 0
visit = [[[False] * n for _ in range(n)] for _ in range(m)]
while(len(target) != 0):
    x,y = target[idx]
    min_rs = INF
    r,c = 0,0
    for b in basecamp:
        xx, yy = b
        rs = bfs(xx, yy, x, y)
        if(rs < min_rs):
            min_rs = rs
            r = xx
            c = yy
    graph[r][c] = -1


        

        
    
    

    
