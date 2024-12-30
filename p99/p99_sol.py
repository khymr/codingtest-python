# import sys
# input = sys.stdin.readline

# max =int(1e9)
# n, k = map(int, input().split())
# lst = [max] * (n+1)
# lst[1] = 0
# for i in range(2,n+1):
#     if(i % k == 0):
#         lst[i] = min(lst[i], lst[i // k] + 1)
#     else:
#         lst[i] = min(lst[i], lst[i-1] + 1)

# print(lst[n])
# N, K공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)