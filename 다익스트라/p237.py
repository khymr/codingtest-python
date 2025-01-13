import sys
input = sys.stdin.readline
INF = int(1e9)


def find_short_path(distance, visit):
    min = INF
    idx = -1
    for i in range(1,n+1):
        if(min > distance[i] and visit[i] == False):
            min = distance[i]
            idx = i
    return idx


def dijkstra(start):
    for i in range(n):
        idx = find_short_path(distance, visit)
        visit[idx] = True
        for g in graph[idx]:
            node, weight = g
            distance[node] = min(distance[node], distance[idx] + weight)




n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
distance = [INF] * (n+1)
start = int(input())

distance[start] = 0


for _ in range(m):
    n1, n2, w = map(int, input().split())
    graph[n1].append((n2, w))

dijkstra(start)
for i in range(1,n+1):
    print(distance[i])



