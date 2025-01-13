import sys
input = sys.stdin.readline

INF = int(1e9)

n,m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))

array = [INF] * 10001
array[0] = 0

# for i in range(1,m+1):
#     for mn in money:
#         if(i % mn == 0):
#             array[i] = min(array[i], array[i-mn] + 1)
#위 주석단 코드는 내가 짰던 코드

for i in range(n):
    for j in range(money[i], m+1):
        if(array[j - money[i]] != INF):
            array[j] = min(array[j], array[j-money[i]] + 1)





if(array[m] != INF):
    print(array[m])
else:
    print(-1)