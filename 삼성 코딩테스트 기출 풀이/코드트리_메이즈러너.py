import sys
import copy

input = sys.stdin.readline
INF = int(1e9)

tot_cnt = 0
n, m, k = map(int, input().split())
graph = []
people = []
exit = (-1, -1)

for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(m + 1):
    a, b = map(int, input().split())
    if i == m:
        exit = (a - 1, b - 1)
    else:
        people.append((a - 1, b - 1))

def move():
    global people, tot_cnt
    new_people = []
    ex, ey = exit
    for x, y in people:
        nx, ny = x, y
        if(ex != x):
            if(ex > x):
                nx +=1
            else:
                nx -=1
            if(0<= nx < n and graph[nx][y] == 0):
                new_people.append((nx, y))
                tot_cnt+=1
                continue
        if(ey != y):
            if(ey > y):
                ny +=1
            else:
                ny -=1
            if(0<= ny < n and graph[x][ny] == 0):
                new_people.append((x, ny))
                tot_cnt+=1
                continue
        new_people.append((x,y))
        


    people = new_people

def distance(p1, p2):
    #p1 = exit p2 = people
    ex, ey = p1
    x, y = p2
    row = abs(ex - x)
    col = abs(ey - y)
    d = max(row, col)
    r = min(ex, x)
    c = min(ey, y)

    if row > col:
        c = max(ey, y) - d
        c = max(c, 0)
    elif row < col:
        r = max(ex, x) - d
        r = max(r, 0)

    return (d, r, c)

def rotate():
    global graph, people, exit

    dist_list = sorted([distance(exit, (x, y)) for x, y in people])
    d, r, c = dist_list[0]

    temp_graph = copy.deepcopy(graph)
    new_exit = exit
    new_people = []
    for i in range(d+1):
        for j in range(d+1):
            new_r, new_c = r + j, c + d - i
            old_r, old_c = r + i, c + j
            if(temp_graph[old_r][old_c] >0):
                temp_graph[old_r][old_c] -=1
            graph[new_r][new_c] = temp_graph[old_r][old_c]
            while (old_r, old_c) in people: 
                people.remove((old_r, old_c))
                new_people.append((new_r, new_c))
            if((old_r, old_c) == exit):
                new_exit = (new_r, new_c)


    people = people + new_people
    exit = new_exit


for _ in range(k):
    move()
    while exit in people:
        people.remove(exit)
    if(len(people) == 0):
        break
    rotate()

print(tot_cnt)
a,b = exit
print(a+1, b+1)