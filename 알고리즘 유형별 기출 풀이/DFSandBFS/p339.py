import sys
input = sys.stdin.readline
from collections import deque

def bfs(depth, start):
    q = deque()
    visit[start] = True
    dpt = 0
    q.append((start, 0))
    rs = []
    while q:
        elem, dpt = q.popleft()
        if(dpt == depth):
            rs.append(elem)
        for e in graph[elem]:
            if(visit[e] == False):
                q.append((e, dpt+1))
                visit[e] = True
                
    if(len(rs) == 0):
        print(-1)
    else:
        rs.sort()
        for r in rs:
            print(r)

        



n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
bfs(k,x)



