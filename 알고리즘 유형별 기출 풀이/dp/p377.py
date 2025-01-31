import sys
input = sys.stdin.readline
#상당히 반례 생각 많이 해아하는 유형
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

answer = [0] * (n+1)
for i in range(n-1, -1, -1):
    day, cost = arr[i][0], arr[i][1]
    if(i + day > n):
        answer[i] = answer[i+1]
        continue
    else:
        answer[i] = max(answer[i+1], cost + answer[i + day])
        
print(answer[0])
