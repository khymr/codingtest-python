import sys
input = sys.stdin.readline
import heapq
from collections import deque
INF = int(1e9)

#다익스트라 풀이
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while(q):
        cost, elem = heapq.heappop(q)
        for g in graph[elem]:
            if(cost > distance[g]):
                continue
            new_cost = cost + 1
            if(new_cost < distance[g]):
                distance[g] = new_cost
                heapq.heappush(q,(distance[g], g))
    
    mx = -1
    idx = -1
    cnt = 0
    for i in range(1,n+1):
        if(mx < distance[i]):
            mx = distance[i]
            idx = i
            cnt = 1
        elif(mx == distance[i]):
            cnt+=1

    print(idx, mx, cnt)
   
        


n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance=  [INF] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dijkstra(1)


#bfs풀이 


# def bfs(graph, start):
#     q = deque()
#     q.append((0,start))
#     visit[start] = True
#     mx_depth = -1
#     idx = -1
#     cnt= 0
#     while q:
#         depth, nd = q.popleft()
#         if(depth > mx_depth):
#             mx_depth = depth
#             idx = nd
#             cnt = 1
#         elif(depth == mx_depth):
#             if(idx > nd):
#                 idx = nd
#             cnt+=1
#         for g in graph[nd]:
#             if(visit[g] == False):
#                 visit[g] = True
#                 q.append((depth+1, g))
#     print(idx, mx_depth, cnt)

# n,m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# visit = [False] * (n+1)
# for _ in range(m):
#     a,b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# bfs(graph, 1)