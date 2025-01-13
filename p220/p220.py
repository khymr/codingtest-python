import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
ans = [0] * n
ans[n-1] = lst[n-1]
ans[n-2] = max(lst[n-1],lst[n-2])
for i in range(len(lst)-3, -1, -1):
    ans[i] = max(ans[i+1], ans[i+2] + lst[i])
print(ans[0])


