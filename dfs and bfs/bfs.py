from collections import deque


def bfs(graph, node, visited):
    q = deque()
    q.append(node)
    visited[node] = True
    result = []
    while q:
        elem = q.popleft()
        result.append(elem)
        for g in graph[elem]:
            if(visited[g] == False):
                visited[g] = True
                q.append(g)
    return result
        



graph = [[], [2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False] * 9

print(bfs(graph, 1, visited))