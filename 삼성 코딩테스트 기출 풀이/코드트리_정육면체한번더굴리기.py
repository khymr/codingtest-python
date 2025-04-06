import sys
input = sys.stdin.readline

dxx = [1,-1, 0,0]
dyy = [0,0,1,-1]
graph = []
def dfs(x, y, visit, ans):
    global cnt
    if(visit[x][y] == True):
        return
    visit[x][y] = True
    
    cnt+=ans
    for i in range(4):
        nx = x + dxx[i]
        ny = y + dyy[i]
        if(0<= nx < n and 0<= ny < n and ans == graph[nx][ny]):
            dfs(nx, ny, visit, ans)


def changeIdx(s):
    if(s < 0):
        s = s + 4
    elif(s >=4):
        s = s - 4
    return s
    

west, top, east, north, south, bottom = 4,1,3,5,2,6

#동, 남, 서, 북
#아랫면이 보드 숫자보다 크면은 +1, 작으면은 -1(-1이거나 4이상이면 3, 0으로 매칭 되도록 구현)
#만약 끝에 다다랐을 때 동이면 += 2처리해줌
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x,y = 0,0
s = 0
n,m = map(int, input().split())

total = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
for _ in range(m):
    nx, ny = x, y
    x += dx[s]
    y += dy[s]
    
    if(x < 0 or x >= n or y < 0 or y >= n):
        s = changeIdx(s+2)
        x = nx + dx[s]
        y = ny + dy[s]

    teast, twest, tsouth, tnorth, ttop, tbottom = east, west, south, north, top, bottom
    if s == 0:  # 동쪽
        top, east, bottom, west = twest, ttop, teast, tbottom
    elif s == 1:  # 남쪽
        top, south, bottom, north = tnorth, ttop, tsouth, tbottom
    elif s == 2:  # 서쪽
        top, west, bottom, east = teast, ttop, twest, tbottom
    elif s == 3:  # 북쪽
        top, north, bottom, south = tsouth, ttop, tnorth, tbottom
    visit = [[False] * n for _ in range(n)]
    cnt =0
    dfs(x, y, visit, graph[x][y])
    total += cnt
    
    if(graph[x][y] < bottom):
        s = changeIdx(s + 1)
        
    elif(graph[x][y] > bottom):
        s = changeIdx(s -1)
    
print(total) 

    


