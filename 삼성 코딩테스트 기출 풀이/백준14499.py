import sys
input = sys.stdin.readline

n,m,x,y,k = map(int, input().split())

east, west, south, north, top, bottom = 0,0,0,0,0,0
#동, 서, 북, 남
dx = [0,0,-1,1]
dy = [1,-1,0,0]
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
direction = list(map(int, input().split()))

for d in direction:
    nx, ny = x,y
    x = x + dx[d-1]
    y = y + dy[d-1]
    if(0 <= x < n and 0<= y < m):
        teast, twest, tsouth, tnorth, ttop, tbottom = east, west, south, north, top, bottom
        if(d == 1):
            west, top, east, bottom = ttop, teast, tbottom, twest
        elif(d == 2):
            west, top, east, bottom = tbottom, twest, ttop, teast
        elif(d == 3):
            north, top, south, bottom = tbottom, tnorth, ttop, tsouth
        else:
            north, top, south, bottom = ttop, tsouth, tbottom, tnorth
        if(lst[x][y] == 0):
            lst[x][y] = bottom
        else:
            bottom = lst[x][y]
            lst[x][y] = 0
        print(top)
    else:
        x,y = nx, ny
    


