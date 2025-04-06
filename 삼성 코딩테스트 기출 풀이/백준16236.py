import sys
input = sys.stdin.readline
from collections import deque
INF = int(1e9)
n = int(input())
dx = [1,-1,0,0]
dy= [0,0,1,-1]

def bfs():
    global x,y
    visit = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visit[x][y] = 0
    
    while q:
        i_x,i_y = q.popleft()
        
        for i in range(4):
            nx = i_x + dx[i]
            ny = i_y + dy[i]
            
            if(0<=nx < n and 0<= ny < n and graph[nx][ny] <= fish):
                if(visit[nx][ny] == -1):
                    visit[nx][ny] = visit[i_x][i_y] + 1
                    q.append((nx, ny))
    
    return visit



def find_init_fish(graph):
    for i in range(n):
        for j in range(n):
            if(graph[i][j] == 9):
                graph[i][j] = 0
                return i,j 
    return 0,0
def find_min_dist(distance):
    min_d = INF
    idx_x, idx_y = 0,0
    gOrStop = 0
    for i in range(n):
        for j in range(n):
            if(distance[i][j] != -1 and (1<=graph[i][j]<fish)):
                if(min_d > distance[i][j]):
                    gOrStop = 1
                    min_d = distance[i][j]
                    idx_x, idx_y = i,j
    if(gOrStop == 0):
        return -1, -1, -1
    return idx_x, idx_y, min_d

    
def change_fish_cnt():
    global fish, cnt
    if(fish <= cnt):
        fish+=1
        cnt = 0


graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
fish = 2
cnt = 0
tot = 0
x,y = find_init_fish(graph)
while True:
    distance = bfs()
    
    
    idx_x, idx_y, min_dist= find_min_dist(distance)
    if(idx_x == -1):
        print(tot)
        break
    graph[idx_x][idx_y] = 0
    tot+= min_dist
    cnt+= 1
    x,y = idx_x, idx_y
    change_fish_cnt()
