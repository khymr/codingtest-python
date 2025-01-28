import sys
input = sys.stdin.readline
import heapq

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))
total = 0

while q:
    if(len(q) == 1):
        break
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    s = a + b
    total += s
    heapq.heappush(q, s)
print(total)



