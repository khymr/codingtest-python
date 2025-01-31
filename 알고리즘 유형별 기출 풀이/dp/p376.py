import sys
input = sys.stdin.readline


n= int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in range(n-2, -1, -1):
    for j in range(i+1):
        lst[i][j] = lst[i][j] + max(lst[i+1][j], lst[i+1][j+1])
print(lst[0][0])



