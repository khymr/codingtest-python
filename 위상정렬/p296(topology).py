from collections import deque
import sys
input = sys.stdin.readline


def topology_sort():
    q = deque()
    for i in range(1,v+1):
        if(indegree[i] == 0):
            q.append(i)
    while q:
        node = q.popleft()
        print(node,  end = ' ')
        for g in graph[node]:
            indegree[g] -=1
            if(indegree[g] == 0):
                q.append(g)
    


v,e = map(int, input().split())

graph = [[] for _ in range(v+1)]

indegree = [0] * (v+1)

for _ in range(e):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    indegree[n2] +=1

topology_sort()

    

