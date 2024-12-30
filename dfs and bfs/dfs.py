
def dfs(graph, node, visited):
    if(visited[node] == True):
        return
    visited[node] = True
    print(node, end = ' ')
    for g in graph[node]:
        dfs(graph, g, visited)

# def dfs(graph, node, visited):
#     visited[node] = True
#     print(node, end = ' ')
#     for g in graph[node]:
#         if(visited[g] == False):
#             dfs(graph, g, visited)

graph = [[], [2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False] * 9

dfs(graph, 1, visited)
print()