import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    result = [0] * (n+1)
    q = deque()
    for i in range(1,n+1):
        if(indegree[i] == 0):
            q.append(i)
            result[i] = cost[i]
            
            
    while q:
        node = q.popleft()
        for g in array[node]:
            indegree[g] -=1
            if(indegree[g] == 0):
                result[g] = max(result[g], result[node] + cost[g])
                q.append(g)
    return result

        




n = int(input())
array = [[] for _ in range(n+1)]
cost = [0] * (n+1)
indegree = [0] * (n+1)
for i in range(1,n+1):
    rs = list(map(int, input().split()))
    cost[i] = rs[0]
    for j in range(1,len(rs)-1):
        array[rs[j]].append(i)
        indegree[i] +=1

ans = topology_sort()
for i in range(1,n+1):
    print(ans[i])


