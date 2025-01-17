import sys
input = sys.stdin.readline

def find_parent(parent, node):
    if(parent[node] != node):
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_parent(parent, a,b):
    p1 = find_parent(parent, a)
    p2 = find_parent(parent, b)
    if(p1 >= p2):
        parent[p1] = p2
    else:
        parent[p2] = p1

n,m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    c,a,b = map(int, input().split())
    if(c):
        if(find_parent(parent, a) == find_parent(parent, b)):
            print("YES")
        else:
            print("NO")
    else:
        union_parent(parent, a,b)
