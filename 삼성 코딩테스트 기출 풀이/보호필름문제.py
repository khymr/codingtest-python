def isOkay(graph):
    for j in range(w):
        cnt = 0
        gOrStop = 0
        for i in range(d-1):
            if(graph[i][j] == graph[i+1][j]):
                cnt+=1
            else:
                cnt = 0
            if(cnt == k-1):
                gOrStop = 1
                break
        if(gOrStop == 0):
            return False
    return True




def dfs(graph, cnt, start):
    global answer
    if(answer <= cnt):
        return
    if(isOkay(graph)):
        if(answer > cnt):
            answer = cnt
        return
    for i in range(start, d):
        group = []
        for j in range(w):
            if(graph[i][j] == 1):
                graph[i][j] = 0
                group.append((i,j))
        dfs(graph, cnt+1, i + 1)
        for g in group:
            x,y = g
            graph[x][y] = 1
        group = []
        for j in range(w):
            if (graph[i][j] == 0):
                graph[i][j] = 1
                group.append((i, j))
        dfs(graph, cnt + 1, i + 1)
        for g in group:
            x, y = g
            graph[x][y] = 0








t = int(input())
for i in range(1,t+1):
    d,w,k = map(int, input().split())
    graph = []
    for _ in range(d):
        graph.append(list(map(int, input().split())))
    if(k == 1):
        print(f'#{i} {0}')

    else:
        answer = int(1e9)
        dfs(graph, 0, 0)
        print(f'#{i} {answer}')
