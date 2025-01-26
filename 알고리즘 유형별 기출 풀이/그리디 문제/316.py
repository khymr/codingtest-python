import sys
import heapq
input = sys.stdin.readline
#개인적으로 어려웠던 문제

def solution(food_times, k):
    if(sum(food_times) <= k):
        return -1
    result = 0
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    prev = 0
    sum_value = 0
    cnt = len(food_times)
    while(sum_value + (q[0][0] - prev) * cnt <= k):
        cur = heapq.heappop(q)[0]
        sum_value += (cur - prev) * cnt
        prev = cur
        cnt -=1
    rs = sorted(q, key = lambda x : x[1])
    result = rs[(k-sum_value) % cnt][1]
    return result






    





food_times = list(map(int, input().split()))
k = int(input())

result = solution(food_times, k)
print(result)




    











