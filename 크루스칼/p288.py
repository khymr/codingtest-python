import sys
input = sys.stdin.readline

def find_parent(parent, node):
    if(parent[node] != node):
        parent[node] = find_parent(parent, parent[node])
    return parent[node]


def union_find(parent, node1, node2):
    p1 = find_parent(parent, node1)
    p2 = find_parent(parent, node2)
    
    if(p1 > p2):
        parent[p1] = p2
    else:
        parent[p2] = p1
    




def cruscal():
    cnt = 0
    total = 0
    for g in q:
        w,n1,n2 = g
        if(find_parent(parent, n1) == find_parent(parent, n2)):
            continue
        union_find(parent, n1, n2)
        cnt+=1
        total += w
        if(cnt == n-1):
            break
    return total

n,m = map(int, input().split())
q = []
parent = [i for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    q.append((c,a,b))
q.sort()

total = cruscal()
print(total)


