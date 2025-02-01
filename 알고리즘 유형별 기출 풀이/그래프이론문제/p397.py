import sys
input = sys.stdin.readline
import heapq

def find_parent(parent,node):
    if(parent[node] != node):
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_find(parent, a, b):
    p1 = find_parent(parent, a)
    p2 = find_parent(parent, b)
    if(p1 > p2):
        parent[p1] = p2
    else:
        parent[p2] = p1
def kruskal():
    cnt = 0
    tot = 0
    while q:
        cost, x, y = heapq.heappop(q)
        if(find_parent(parent, x) == find_parent(parent, y)):
            continue
        print(cost)
        cnt+=1
        tot += cost
        union_find(parent, x, y)
        if(cnt == n-1):
            break
    return tot
    


n,m = map(int, input().split())
q = []
parent = [i for i in range(n)]
tot = 0
for _ in range(m):
    x,y,z = map(int, input().split())
    heapq.heappush(q, (z,x,y))
    tot+=z

ans = kruskal()
print(tot-ans)
