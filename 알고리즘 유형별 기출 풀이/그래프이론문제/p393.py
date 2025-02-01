import sys
input = sys.stdin.readline

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
    return True

n,m = map(int,input().split())

graph = []
parent = [i for i in range(n)]
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(i+1, n):
        if(graph[i][j] == 1):
            union_find(parent, i, j)

            

city = list(map(int, input().split()))

prev = city[0]
no = 0
for i in range(1,m):
    if(find_parent(parent, prev-1) != find_parent(parent, city[i]-1)):
        no = 1
        break
    prev = city[i]
if(no):
    print("NO")
else:
    print("YES")










