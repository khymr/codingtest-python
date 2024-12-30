import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, x,y):
    q = deque()
    q.append((x,y,1))
    graph[x][y] = 0
    while q:
        a,b,cnt = q.popleft()
        if(a == n-1 and b == m-1):
            return cnt
        for i in range(4):
            mx = a + dx[i]
            my = b + dy[i]
            if(mx < 0 or mx > n-1 or my < 0 or my > m-1):
                continue
            
            if(graph[mx][my] == 0):
                continue
            graph[mx][my] = 0
            q.append((mx, my, cnt + 1))

dx = [1,-1,0,0]
dy = [0,0,1,-1]


n,m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().rstrip())))
count = bfs(lst, 0, 0)
print(count)


