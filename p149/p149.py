import sys
input = sys.stdin.readline

def dfs(graph, i, j):
    if(graph[i][j] == 1):
        return
    graph[i][j] = 1
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if(x < 0 or x > n-1 or y < 0 or y > m-1):
            continue
        dfs(graph, x, y)


dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
cnt = 0
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 0):        
            cnt+=1
            dfs(graph, i, j)

        else:
            continue

print(cnt)

