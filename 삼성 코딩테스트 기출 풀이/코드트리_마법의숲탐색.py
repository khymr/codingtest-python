import sys
input = sys.stdin.readline
from collections import deque

r,c,k = map(int, input().split())
r-=1
c-=1
direction_x = [-1,0,0,1]
direction_y = [0,1,1,0]
def valid_row(idx):
    if(0<= idx < r):
        return True
    return False
def valid_col(idx):
    if(0<= idx < c):
        return True
    return False

def valid_low(graph, i, j):
    if(valid_row(i+1) and valid_col(j-1) and valid_col(j+1) and valid_row(i+2)):
        if(graph[i+1][j-1] == 0 and graph[i+1][j+1] == 0 and graph[i+2][j] == 0):
            return True
        else:
            return False
    else:
        return False
    
def valid_west(graph, i, j):
    if(valid_row(i-1) and valid_col(j-1)and valid_col(j-2) and valid_row(i+1)
       and valid_row(i+2)):
        if(graph[i-1][j-1] == 0 and graph[i][j-2] == 0 and graph[i+1][j-2] == 0
        and graph[i+1][j-1] == 0 and graph[i+2][j-1] == 0):
            return True
        else:
            return False
    else:
        return False


def valid_east(graph, i, j):
    if(valid_row(i-1) and valid_row(i+1) and valid_row(i+2)
       and valid_col(j+1) and valid_col(j+2)):
        
        if(graph[i-1][j+1] == 0 and graph[i][j+2] == 0 and graph[i+1][j+1] == 0
        and graph[i+1][j+2] == 0 and graph[i+2][j+1] == 0):
            return True
        else:
            return False
    else:
        return False

def make_west_dir(d):
    d-=1
    if(d < 0):
        d += 4
    return d
def make_east_dir(d):
    d+=1
    if(d > 3):
        d-=4
    return d
def change_graph(graph, x, y, dir):
    graph[x][y] = 3#center는 3으로 처리
    for k in range(4):
        nx = x + direction_x[k]
        ny = y + direction_y[k]
        if(k == dir):
            graph[nx][ny] = 2 # 출구 차별화 처리
        else:
            graph[nx][ny] = 1
    

def bfs(graph, c, d):
    global tot_cnt
    x,y = 0,c
    q = deque()
    visit = [[False] * c for _ in range(r)]
    q.append((x,y,d))
    visit[x][y] = True
    gOrStop = 0
    while q:
        
        x,y,d = q.popleft()
        if(valid_low(graph, x, y)):
            q.append((x+1,y,d))
            continue
        if(valid_west(graph, x, y)):
            q.append((x+1, y-1, make_west_dir(d)))
            continue
        if(valid_east(graph, x, y)):
            q.append((x+1, y+1, make_east_dir(d)))
        if(x < 0):
            gOrStop = 1
            break
    if(gOrStop == 1):
        graph = [[0] * c for _ in range(r)]  # 격자 초기화
        return False


    change_graph(graph, x,y, d)
    if(x == r-1):
        tot_cnt+=(x+2)
    else:
        
        for k in range(4):
            nx = x + direction_x[k]
            ny = y + direction_y[k]
            if(graph[nx][ny] == 2):
                max_x = -1
                for kk in range(4):
                    kx = nx + direction_x[kk]
                    ky = ny + direction_y[kk]
                    if(0<= kx < r and 0<= ky < c):
                        if(graph[kx][ky] == 3 and kx,ky != x,y):
                            if(max_x < kx):
                                max_x = kx
                               
                break  
        tot_cnt+= (max_x + 2)        

    return True
    



tot_cnt = 0
golumm = []
for _ in range(k):
    c,d = map(int, input().split())
    golumm.append((c-1, d))
graph = [[0] * c for _ in range(r)]
for g in golumm:
    c,d = g
    bool = bfs(graph, c,d)
    if(bool == False):
        bfs(graph, c,d)
        




