import sys
input = sys.stdin.readline
#from math import factorial


# def combination(n, r):
#     return factorial(n) // (factorial(r) * factorial(n - r))

# n,m = map(int, input().split())
# array = [0] * (m+1)
# weight = list(map(int, input().split()))

# for w in weight:
#     array[w] +=1
# ans = combination(n,2)
# for i in range(1, len(array)):
#     if(array[i] != 1):
#         ans -= combination(array[i],2)
# print(ans)

n,m = map(int, input().split())
weight = list(map(int, input().split()))

ans = [0] * (m+1)
for w in weight:
    ans[w]+=1
result = 0
for i in range(1,m+1):
    n -= ans[i]
    result +=(ans[i] * n)
print(result) 


