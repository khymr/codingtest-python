import sys
input = sys.stdin.readline
import copy
dx = [1,-1,0,0]
dy =[0,0,1,-1]

ddx = [-1,1,1,-1]
ddy = [-1,-1,1,1]

n,m,k,c = map(int, input().split())


def grow():
    position = []
    global graph
    for i in range(n):
        for j in range(n):
            if(graph[i][j] > 0):
                position.append((i,j))
                cnt1 = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if(0<= nx < n and 0<= ny< n):
                        if(graph[nx][ny] > 0):
                            cnt1+=1
                graph[i][j] += cnt1
    
    return position

def grow_near(position):
    global graph ,c_position
    array = copy.deepcopy(graph)
    for p in position:
        x,y = p
        cnt2 = 0
        tmp = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<= nx < n and 0<= ny < n):
                if(array[nx][ny] == 0 and c_position[nx][ny] == 0):
                    cnt2+=1
                    tmp.append((nx, ny))
        if(cnt2 == 0):
            continue
        elem = graph[x][y] // cnt2
        for t in tmp:
            a,b = t
            graph[a][b] += elem
            

def dfs():
    global graph
    max_c = -1
    pos = []
    for i in range(n):
        for j in range(n):
            tmp = []
            cnt =0
            if(graph[i][j] > 0):
                
                cnt+= graph[i][j]
                
                tmp.append((i,j))

                for d in range(4):
                    nx, ny = i,j
                    for _ in range(k):
                        nx+= ddx[d]
                        ny+= ddy[d]
                        if(0<= nx < n and 0<= ny < n):
                            if(graph[nx][ny] == 0):
                                tmp.append((nx,ny))
                                break
                            elif(graph[nx][ny] > 0):
                                cnt+= graph[nx][ny]
                                tmp.append((nx,ny))
                            elif graph[nx][ny] ==-1:
                                # 벽 만나면
                                break
                        else:
                            break
            if(max_c < cnt):
                max_c = cnt
                pos = tmp
    return max_c, pos

    
def kill(pos):
    global graph, c_position
    for i in range(n):
        for j in range(n):
            if(c_position[i][j] > 0):
                c_position[i][j] -=1
    for cp in pos:
        x,y = cp
        c_position[x][y] = c
        graph[x][y] = 0


graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
c_position = [[0] * n for _ in range(n)]
total = 0
cm = 0
poss = []
for _ in range(m):
    position = grow()
    grow_near(position)
    cm, poss = dfs()
    kill(poss)
    total += cm
    
    
print(total)
    

    
