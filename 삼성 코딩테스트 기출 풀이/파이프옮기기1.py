import sys
input = sys.stdin.readline


def dfs(graph, x, y, direction):
    global cnt
    if(x == n-1 and y == n-1):
        cnt+=1
    #가로
    if(direction == 0):
        if(y < n-1 and graph[x][y+1] == 0):
            dfs(graph, x, y+1, 0)
        if(x < n-1 and y < n-1):
            if(graph[x+1][y] == 0 and graph[x+1][y+1] == 0 and graph[x][y+1] == 0):
                dfs(graph,x+1,y+1,2)
    

        

    #세로
    elif(direction == 1):
        if(x < n-1 and graph[x+1][y] == 0):
            dfs(graph, x+1, y, 1)
        if(x < n-1 and y < n-1):
            if(graph[x+1][y] == 0 and graph[x+1][y+1] == 0 and graph[x][y+1] == 0):
                dfs(graph,x+1,y+1,2)
        

    #대각선
    elif(direction == 2):
        if(y < n-1 and graph[x][y+1] == 0):
            dfs(graph, x, y+1, 0)
        if(x < n-1 and graph[x+1][y] == 0):
            dfs(graph, x+1, y, 1)
        if(x < n-1 and y < n-1):
            if(graph[x+1][y] == 0 and graph[x+1][y+1] == 0 and graph[x][y+1] == 0):
                dfs(graph,x+1,y+1,2)
    
        



n= int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
direction = 0
cnt = 0
dfs(graph,0,1,direction)
print(cnt)