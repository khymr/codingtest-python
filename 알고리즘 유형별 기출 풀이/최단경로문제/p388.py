import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)
dx = [1,-1, 0, 0]
dy = [0,0,1,-1]
t= int(input())
for _ in range(t):
    n = int(input())
    array = []
    for _ in range(n):
        array.append(list(map(int, input().split())))
    distance = [[INF] * (n) for _ in range(n)]
    q = []
    heapq.heappush(q, (array[0][0], 0, 0))
    distance[0][0] = array[0][0]
    while(q):
        cost, x, y = heapq.heappop(q)
        if(cost > distance[x][y]):
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<n and 0<=ny<n):
                new_cost = cost + array[nx][ny]
                if(new_cost < distance[nx][ny]):
                    distance[nx][ny] = new_cost
                    heapq.heappush(q, (distance[nx][ny], nx, ny))
    print(distance[n-1][n-1])

        
        


