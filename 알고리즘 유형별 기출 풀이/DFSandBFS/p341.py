import sys
input = sys.stdin.readline
from itertools import combinations
import copy
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(graph, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if(graph[nx][ny] == 0):
                graph[nx][ny] = 2
                dfs(graph, nx, ny)




n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


indexes = [(i,j) for i in range(n) for j in range(m)]
combination_lists = list(combinations(indexes, 3))
mx = 0
for c in combination_lists:
    idx1_x, idx1_y, idx2_x, idx2_y, idx3_x, idx3_y = c[0][0],c[0][1],c[1][0],c[1][1],c[2][0],c[2][1]
    
    if(data[idx1_x][idx1_y] == 0 and data[idx2_x][idx2_y] == 0 and data[idx3_x][idx3_y] == 0):
        data[idx1_x][idx1_y] = data[idx2_x][idx2_y] = data[idx3_x][idx3_y] = 1
        dcpy = copy.deepcopy(data)
        sum = 0
        for i in range(n):
            for j in range(m):
                if(dcpy[i][j] == 2):
                    dfs(dcpy, i, j)
        for i in range(n):
            for j in range(m):
                if(dcpy[i][j] == 0):
                    sum+=1
        if(mx < sum):
            mx = sum
        data[idx1_x][idx1_y] = data[idx2_x][idx2_y] = data[idx3_x][idx3_y] = 0
print(mx)

        

        
        


