import sys
input = sys.stdin.readline
import heapq

def find_parent(parent, node):
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
        if(find_parent(parent, x) != find_parent(parent,y)):
            union_find(parent, x, y)
            tot+= cost
            cnt+=1
        if(cnt == n-1):
            break
        
    return tot



n = int(input())
graph = []
x = []
y = []
z = []
parent = [i for i in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    
    x.append((graph[i][0], i))
    y.append((graph[i][1], i))
    z.append((graph[i][2],i))
x.sort()
y.sort()
z.sort()
q = []
for i in range(1,n):
    heapq.heappush(q, (abs(x[i-1][0]-x[i][0]), x[i-1][1],x[i][1]))
    heapq.heappush(q, (abs(y[i-1][0]-y[i][0]), y[i-1][1],y[i][1]))
    heapq.heappush(q, (abs(z[i-1][0]-z[i][0]), z[i-1][1],z[i][1]))
print(kruskal())


        







