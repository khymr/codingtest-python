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
    

g = int(input())
p = int(input())

parent = [i for i in range(g+1)]
cnt = 0
for _ in range(p):
    elem = int(input())
    data = find_parent(parent, elem)
    if(data == 0):
        break
    cnt+=1
    union_find(parent, data, data-1)
print(cnt)


