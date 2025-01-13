import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    n1, n2, w = map(int, input().split())
    graph[n1][n2] = w

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j], end = ' ')
    print()

