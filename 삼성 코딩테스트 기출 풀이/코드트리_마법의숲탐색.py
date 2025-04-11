# import sys
# input = sys.stdin.readline
# from collections import deque
# R,C,K = map(int, input().split())

# dx =[-1, 0, 1, 0]
# dy =[0, 1, 0, -1]
# def correct_idx(x,y):
#     if(3<=x < R+3 and 0<=y<C):
#         return True
#     return False
# #다운은 남, 서, 동 순으로 
# #서 이면 d 는 반시계(-1) 동이면 d는 시계 남이면 유지

# def valid_row(idx):
#     if(0<= idx < R+3):
#         return True
#     return False
# def valid_col(idx):
#     if(0<= idx < C):
#         return True
#     return False

# def valid_south(graph, x, y):
#     if(valid_row(x) and valid_col(y-1) and valid_row(x+1) and valid_col(y)
#        and valid_col(y+1)):
#         if(graph[x][y-1] == 0 and graph[x+1][y] == 0 and graph[x][y+1] == 0):
#             return True
#     return False

# def valid_west(graph, x, y):
#     if(valid_row(x) and valid_col(y) and valid_col(y-1) and valid_row(x-1)
#        and valid_row(x-2) and valid_row(x+1)):
#         if(graph[x][y] == 0 and graph[x][y-1] == 0 and graph[x-1][y-1] == 0 and graph[x-2][y] == 0 
#         and graph[x+1][y] == 0):
#             return True
#     return False


# def valid_east(graph, x, y):
#     if(valid_row(x) and valid_col(y) and valid_row(x+1) and valid_col(y+1)
#        and valid_row(x-1) and valid_row(x-2)):
#         if(graph[x][y] == 0 and graph[x+1][y] == 0 and graph[x][y+1] == 0 and graph[x-1][y+1] == 0 
#         and graph[x-2][y] == 0):
#             return True
#     return False


# def down(graph, x, y, d, id):
#     while True:
#         if(valid_south(graph,x+1, y)):
#             x = x+1
#         elif(valid_west(graph, x+1, y-1)):
#             x = x+1
#             y = y-1
#             d = (d-1) % 4
#         elif(valid_east(graph, x+1, y+1)):
#             x = x+1
#             y = y+1
#             d = (d+1) % 4
#         else:
#             break
#     return x, y, d

# def clear_all():
#     global graph, exit
#     for i in range(R+3):
#         for j in range(C):
#             graph[i][j] = 0 
#             if(exit[i][j] == True):
#                 exit[i][j] = False
    
# def change_graph(graph, x, y, d, id):
#     global exit
#     graph[x][y] = id
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         graph[nx][ny] = id
#         if(k == d):
#             exit[nx][ny] = True
    

# def move_elf(graph, x, y):
#     global exit
#     visit = [[False] * C for _ in range(R+3)]
#     q = deque()
#     q.append((x,y))
#     visit[x][y] = True
#     max_x = 0
#     while q:
#         x,y = q.popleft()
#         max_x = max(x, max_x)
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if(visit[nx][ny]==True):
#                 continue
#             if(graph[nx][ny] == graph[x][y] or (graph[nx][ny] > 0 and exit[nx][ny] == True)):
#                 q.append((nx, ny))
#                 visit[nx][ny] = True
#     return max_x -2

# graph = [[0] * (C) for _ in range(R+3)]
# answer = 0
# golumn = []
# for id in range(1,K+1):
#     ci,d = map(int, input().split())
# golumn.append((ci-1, d))
# exit = [[False] * (C) for _ in range(R+3)]
# id = 0   
# for g in golumn:
#     id+=1
#     ci,d = g
#     x,y,d = down(graph,0,ci,d,id)
#     if(not correct_idx(x,y)):
#         clear_all()
#     else:
#         change_graph(graph, x, y, d, id)
#         answer+= move_elf(graph, x, y) 
    
# print(answer)

import sys
input = sys.stdin.readline
from collections import deque

R, C, K = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def correct_idx(x, y):
    return 3 <= x < R + 3 and 0 <= y < C

def valid_row(idx):
    return 0 <= idx < R + 3

def valid_col(idx):
    return 0 <= idx < C

def valid_south(graph, x, y):
    if valid_row(x+2) and valid_col(y-1) and valid_col(y+1):
        if graph[x+1][y-1] == 0 and graph[x+1][y] == 0 and graph[x+1][y+1] == 0 and graph[x+2][y] == 0:
            return True
    return False

def valid_west(graph, x, y):
    if valid_row(x+2) and valid_col(y-2):
        if graph[x][y-1] == 0 and graph[x+1][y-1] == 0 and graph[x+2][y-1] == 0 and graph[x+1][y-2] == 0 and graph[x+2][y-2] == 0:
            return True
    return False

def valid_east(graph, x, y):
    if valid_row(x+2) and valid_col(y+2):
        if graph[x][y+1] == 0 and graph[x+1][y+1] == 0 and graph[x+2][y+1] == 0 and graph[x+1][y+2] == 0 and graph[x+2][y+2] == 0:
            return True
    return False

def down(graph, x, y, d, id):
    while True:
        if valid_south(graph, x, y):
            x += 1
        elif valid_west(graph, x, y):
            x, y, d = x + 1, y - 1, (d - 1) % 4
        elif valid_east(graph, x, y):
            x, y, d = x + 1, y + 1, (d + 1) % 4
        else:
            break
    return x, y, d

def clear_all():
    global graph, exits
    for i in range(R+3):
        for j in range(C):
            graph[i][j] = 0
            exits[i][j] = False

def change_graph(graph, x, y, d, id):
    global exits
    graph[x][y] = id
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if valid_row(nx) and valid_col(ny):
            graph[nx][ny] = id
    exits[x + dx[d]][y + dy[d]] = True

def move_elf(graph, x, y):
    global exits
    visit = [[False] * C for _ in range(R+3)]
    q = deque([(x, y)])
    visit[x][y] = True
    max_x = x
    while q:
        x, y = q.popleft()
        max_x = max(max_x, x)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not valid_row(nx) or not valid_col(ny) or visit[nx][ny]:
                continue
            if graph[nx][ny] == graph[x][y] or (graph[nx][ny] > 0 and exits[x][y]):
                q.append((nx, ny))
                visit[nx][ny] = True
    return max_x - 2

graph = [[0] * C for _ in range(R+3)]
exits = [[False] * C for _ in range(R+3)]
answer = 0

for id in range(1, K+1):
    ci, d = map(int, input().split())
    ci -= 1
    x, y, d = down(graph, 0, ci, d, id)
    if not correct_idx(x, y):
        clear_all()
        continue
    change_graph(graph, x, y, d, id)
    answer += move_elf(graph, x, y)

print(answer)


