import sys
input = sys.stdin.readline

def find_parent(parent, node):
    if(parent[node] != node):
        parent[node] = find_parent(parent, parent[node])
    return parent[node]
    

def union_find(parent, n1, n2):
    p1 = find_parent(parent, n1)
    p2 = find_parent(parent, n2)

    if(p1 >= p2):
        parent[p1] = p2
    else:
        parent[p2] = p1
    

n,m = map(int, input().split())

parent = [i for i in range(n+1)]


for _ in range(m):
    a,b= map(int, input().split())
    union_find(parent, a, b)
for i in range(1,n+1):
    print(find_parent(parent, i), end = ' ')
print()
for i in range(1,n+1):
    print(parent[i], end = ' ')
print()


