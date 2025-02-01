import sys
input = sys.stdin.readline
from collections import deque


def topology_sort(graph):
    
    q = deque()
    cnt=  0
    rs = []
    for i in range(1,n+1):
        if(indegree[i] == 0):
            q.append(i)
            cnt+=1
    if(cnt > 1):
        print("?")
        return
    while q:
        node = q.popleft()
        rs.append(node)
        cnt = 0
        for g in graph[node]:
            indegree[g]-=1
            if(indegree[g] == 0):
                cnt+=1
                q.append(g)
        if(cnt > 1):
            print("?")
            return   
    if(len(rs) != n):
        print("IMPOSSIBLE")
        return
    for i in range(n):
        print(rs[i], end = ' ')
    print()
    

                
    
        
            


t = int(input())
for _ in range(t):
    
    n = int(input())
    team = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for i in range(n):
        for j in range(i+1,n):
            graph[team[i]].append(team[j])
            indegree[team[j]]+=1
    m = int(input())
    for _ in range(m):
        a,b = map(int, input().split())
        if(graph[a].count(b) == 0):
            graph[a].append(b)
            indegree[a]-=1
            graph[b].remove(a)
            indegree[b]+=1
        else:
            graph[b].append(a)
            indegree[b]-=1
            graph[a].remove(b)
            indegree[a]+=1
    topology_sort(graph)

