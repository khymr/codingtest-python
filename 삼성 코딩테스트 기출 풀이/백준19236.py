import sys
input = sys.stdin.readline
import copy

dx = [-5,-1,-1,0,1,1,1,0,-1]
dy = [-5,0,-1,-1,-1,0,1,1,1]

def one_direction(direction):
    if(direction > 8):
        direction = direction%8
    return direction
def find_fish(array, idx):
    for i in range(4):
        for j in range(4):
            if(array[i][j][0] == idx):
                return (i,j)
    return None

def move_all_fish(array, now_x, now_y):
    for i in range(1,17):
        position = find_fish(array, i)
        if(position != None):
            x,y = position
            fish,dir = array[x][y]
            
            
            for _ in range(8):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == now_x and ny == now_y):
                    array[x][y] = (fish, dir)
                    array[nx][ny], array[x][y] = array[x][y], array[nx][ny]
                    break
                dir = one_direction(dir + 1)
    
def get_possible_position(array, now_x, now_y, d):
    positions = []
    i = now_x
    j = now_y
    while True:
        i += dx[d]
        j += dy[d]
        if not (0 <= i < 4 and 0 <= j < 4):
            break
        if(array[i][j][0] != -1):
            positions.append((i,j))
    

    return positions



def dfs(graph, now_x, now_y, total):
    global result
    array = copy.deepcopy(graph)
    fish, direction = array[now_x][now_y]
    total += fish
    array[now_x][now_y] = (-1,-1)
    move_all_fish(array, now_x, now_y)

    positions = get_possible_position(array, now_x, now_y,direction)
    if(len(positions) == 0):
        result= max(result, total)
        return
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)



graph = [[] for _ in range(4)]
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(0, len(tmp), 2):
        graph[i].append((tmp[j], tmp[j+1]))
result = 0
dfs(graph, 0,0,0)
print(result)





    




        
        