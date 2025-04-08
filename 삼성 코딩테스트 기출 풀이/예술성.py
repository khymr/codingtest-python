import sys
input = sys.stdin.readline
from itertools import combinations
import copy

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def dfs(graph, i, j,elem):
    global cm
    if(visit[i][j] == True):
        return
    cm.append((i,j))
    visit[i][j] = True
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if(0<= nx < n and 0 <= ny < n and graph[nx][ny] == elem):
            dfs(graph, nx, ny,elem)
def validation_check(comb, i, j):
    cnt1 = 0
    for ci in comb[i]:
        x,y = ci
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if(0<= nx < n and 0<= ny < n):
                if((nx, ny) in comb[j]):
                    cnt1+=1
    return cnt1



def calculate_point(idxs, comb, graph):
    global tot_point
    for c in idxs:
        a,b = c
        rs = validation_check(comb, a, b)
        if(rs == 0):
            continue
        else:
            ca, cb = comb[a], comb[b]
            len_a = len(ca)
            len_b = len(cb)
            tx, ty = ca[0][0], ca[0][1]
            elem_a = graph[tx][ty]
            tx, ty = cb[0][0], cb[0][1]
            elem_b = graph[tx][ty]
            point = (len_a + len_b)*elem_a*elem_b*rs
            tot_point+=point

def rotate_mid():
    global graph
    tmp = copy.deepcopy(graph)
    mid = n // 2
    for i in range(n):
        graph[i][mid] = tmp[mid][n-i-1]
        graph[mid][i] = tmp[i][mid]
    

def rotate_blocks():
    tmp = copy.deepcopy(graph)
    half = n // 2
    starts = [(0,0), (0,half+1), (half+1, 0), (half+1, half+1)]
    for sr, sc in starts:
        for i in range(half):
            for j in range(half):
                graph[sr+j][sc + half -1 - i] = tmp[sr+i][sc+j]



# 전체 회전
def rotate_all():
    rotate_mid()
    rotate_blocks()




    
tot_point = 0
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for _ in range(4):
    visit = [[False] * (n) for _ in range(n)]
    comb = []
    for i in range(n):
        for j in range(n):
            if(visit[i][j] == False):
                cm = []
                dfs(graph, i, j, graph[i][j])
                comb.append(cm)
    l = len(comb)
    lst = [i for i in range(l)]
    idxs = list(combinations(lst, 2))
    calculate_point(idxs,comb, graph)
    rotate_all()
    
print(tot_point)
    

