import sys
input = sys.stdin.readline
import copy
n = 5
d =3
cnt_for_dfs = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
visit = []

def fill_blank(graph, new_elem, wall):
    global idx
    new_elem.sort(key=lambda x : (x[1], -x[0]))
    for e in new_elem:
        x,y = e
        graph[x][y] = wall[idx]
        idx+=1



def turn_90(g, r, c):
    new_g = copy.deepcopy(g)
    for i in range(d):
        for j in range(d):
            new_g[r + j][c + d - i-1] = g[r + i][c + j]
    return new_g
    

def dfs(g, i, j,ans, elem): 
    global cnt_for_dfs
    global visit
    if(visit[i][j] == True):
        return
    cnt_for_dfs+=1
    
    visit[i][j] = True
    elem.append((i,j))
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        
        if(0<= nx < n and 0<= ny < n):
            if(visit[nx][ny] ==False and g[nx][ny] == ans):
                
                dfs(g, nx, ny, ans,elem)
                  

def point_calculate(g):
    global cnt_for_dfs
    global visit
    return_cnt = 0
    return_elem = []
    visit = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cnt_for_dfs = 0
            tmp_elem = []
            if(visit[i][j] == False):
                dfs(g, i, j, g[i][j], tmp_elem)
                if(cnt_for_dfs >=3):
                    return_cnt+= cnt_for_dfs
                    for te in tmp_elem:
                        return_elem.append(te)
    return return_elem, return_cnt



def find_value(graph, i, j):
    global order
    
    tmp = copy.deepcopy(graph)
    degree = 90
    for _ in range(3):
        tmp = turn_90(tmp, i, j)
        
        elem, ct = point_calculate(tmp)
        if(ct > 0):
            order.append((ct, degree,j,i,tmp,elem))
        degree+=90
    #카운트, 각도, 열, 행, 그래프, 0으로 바꿀 요소 값들

        




k,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
wall = list(map(int, input().split()))
#find_value에서 3개 돌려버리기
#point_calculate에서 계산된  요소값 반환하도록 코딩

idx = 0
for _ in range(k):
    order = []
    tot_cnt = 0
    new_g = []
    new_elem = []
    for i in range(n):
        for j in range(n):
            if(j + d > n or i + d > n):
                continue
            find_value(graph, i, j)
    if(len(order) == 0):
        break
    order.sort(key= lambda x: (-x[0], x[1], x[2], x[3]))
    #카운트, 각도, 열, 행, 그래프, 0으로 바꿀 요소 값들
    cnt, degree, co,ro,new_g, new_elem = order[0]  
    graph = new_g
    tot_cnt+=cnt
    
    fill_blank(graph, new_elem, wall)
    
    while(True):
        elem, cnt2 = point_calculate(graph)
        if(len(elem) > 0):
            tot_cnt += cnt2
            fill_blank(graph, elem,wall)
        else:
            break
    print(tot_cnt, end = ' ')