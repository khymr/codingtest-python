import sys
input = sys.stdin.readline
from itertools import combinations
INF = int(1e9)

def dist(hx, hy, cx, cy):
    return abs(hx-cx) + abs(hy-cy)

n,m = map(int, input().split())

chicken = []
house = []
cnt = 0
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        if(lst[j] == 1):
            house.append((i,j))
        elif(lst[j] == 2):
            chicken.append((i,j))
            cnt+=1
           
total = []
new_chicken = list(combinations(chicken, m))
for nc in new_chicken:
    
    result = []
    for h in house:
        hx, hy = h
        min = INF
        for c in nc:
            cx, cy = c
            elem = dist(hx, hy, cx, cy)
            if(min > elem):
                min = elem
        result.append(min)
    total.append(sum(result))
total.sort()
print(total[0])
        


    
