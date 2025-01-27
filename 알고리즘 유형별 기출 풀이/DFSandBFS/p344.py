import sys
input = sys.stdin.readline
from collections import deque
import heapq
#나는 heapq도입했는데 그냥 리스트에 넣고 sort해도 된다
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(graph, depth,idx_x, idx_y):
    q = deque()
    rs = []
    for i in range(n):
        for j in range(n):
            if(lst[i][j] != 0):
                heapq.heappush(rs,(lst[i][j], i,j))
                
    while rs:
        elem, x, y = heapq.heappop(rs)
        q.append((x,y,0))
    

    while q:
        x, y, depth = q.popleft()
        if(depth == s):
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(0<= nx < n and 0<=ny<n):
                if(graph[nx][ny] == 0):
                    graph[nx][ny] = graph[x][y]
                    q.append((nx, ny, depth+1))
        
    return graph[idx_x][idx_y]
    
    
    



n,k = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
s,x,y = map(int, input().split())

ans = bfs(lst,s, x-1,y-1)
print(ans)

