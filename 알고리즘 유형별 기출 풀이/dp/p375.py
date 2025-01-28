import sys
input = sys.stdin.readline

t = int(input())

dx = [-1,0,1]
dy = [-1,-1,-1]




for _ in range(t):
    n,m = map(int, input().split())
    graph = []
    lst = list(map(int, input().split()))
    idx = 0
    for _ in range(n):
        graph.append(lst[idx:idx+m])
        idx+=m
    for j in range(1,m):
        
        for i in range(n):
            mx = 0
            for k in range(3):
                nx = i + dx[k]
                ny = j + dy[k]
                if(0<=nx<n and 0<=ny<m):
                    mx = max(mx, graph[i][j] + graph[nx][ny])
            graph[i][j] = mx
    ans = 0
    for i in range(n):
        ans = max(graph[i][m-1], ans)
    print(ans)




    
          


    