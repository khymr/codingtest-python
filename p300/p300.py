import sys
input = sys.stdin.readline

def find_parent(parent, node):
    if(parent[node] != node):
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_parent(parent, a,b):
    p1 = find_parent(parent, a)
    p2 = find_parent(parent, b)
    if(p1 == p2):
        return False
    elif(p1 > p2):
        parent[p1] = p2
    else:
        parent[p2] = p1
    return True

def kruscal():
    cnt = 0
    result = []
    for i in range(len(array)):
        c,a,b = array[i]
        if(union_parent(parent, a,b) == True):
            cnt+=1
            result.append(c)
        if(cnt == n-1):
            break
    return sum(result) - result[len(result)-1]



n,m = map(int, input().split())
parent = [i for i in range(n+1)]
array = []
for _ in range(m):
    a,b,c = map(int, input().split())
    array.append((c,a,b))
array.sort()

rs = kruscal()
print(rs)