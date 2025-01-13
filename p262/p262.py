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
        if(distance[node] < weight):
            continue
        for g in graph[node]:
            gw, gn = g
            if(distance[gn] > distance[node] + gw):
                distance[gn] = distance[node] + gw
                heapq.heappush(q, (distance[gn], gn))

n,m,c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    ma,mb,mc = map(int, input().split())
    graph[ma].append((mc,mb))
dijkstra(c)

cnt = 0
m_d = -1
for d in distance:
    if(d == INF or d == 0):
        continue
    else:
        cnt+=1
        if(m_d < d):
            m_d = d
print(cnt, m_d)


