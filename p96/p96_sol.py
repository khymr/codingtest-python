import sys
input = sys.stdin.readline

n,m = map(int, input().split())
min_max = 0
for _ in range(n):
    lst = list(map(int, input().split()))
    mn = min(lst)
    if(min_max < mn):
        min_max = mn
print(min_max)

