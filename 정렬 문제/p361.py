import sys
input = sys.stdin.readline
#sum으로 해도 되지만 실제로 그냥 len길이에서 감소시키면서 하는게 더 효율적으로 보임
#주석단 코드 참고
def solution(N, stages):
    stages.sort()
    result = [0] * (N+2)
    for s in stages:
        result[s]+=1
    for i in range(1,len(result)-1):
        if(sum(result[i:]) == 0):
            result[i] = 0
            break
        result[i] = result[i] / sum(result[i:])
    rs = []
    for i in range(1,N+1):
        rs.append((result[i], i))
    rs.sort(key=lambda x : (-x[0], x[1]))
    answer = []
    for r in rs:
        answer.append(r[1])
    return answer


# def solution(N, stages):
#     stages.sort()
#     result = [0] * (N+2)
#     for s in stages:
#         result[s] += 1

#     total_players = len(stages)
#     failure_rates = []

#     for i in range(1, N+1):
#         if total_players > 0:
#             failure_rate = result[i] / total_players
#             total_players -= result[i]
#         else:
#             failure_rate = 0
#         failure_rates.append((failure_rate, i))

#     failure_rates.sort(key=lambda x: (-x[0], x[1]))

#     answer = [stage for _, stage in failure_rates]
#     return answer





   


n = int(input())
stages = list(map(int, input().split()))
result = solution(n, stages)
print(result)

