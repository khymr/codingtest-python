import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        weight, node = heapq.heappop(q)
        if(distance[node] < weight):  #주의
            continue
        for g in graph[node]:
            aw, an = g
            if(distance[an] > distance[node] + aw):
                distance[an] = distance[node] + aw
                heapq.heappush(q, (distance[an], an))

        
        

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
start = int(input())

for _ in range(m):
    n1, n2, w = map(int, input().split())
    graph[n1].append((w, n2))

dijkstra(start)
for i in range(1,n+1):
    print(distance[i])

