import sys
input = sys.stdin.readline

#파이썬 int내장함수가 음수 몫연산을 처리해준다
def dfs(depth, now, plus, minus, mul, div):
    
    global mx, mn
    if(depth == n):
        mx = max(mx, now)
        mn = min(mn, now)
        return
    if(plus != 0):
        dfs(depth+1, now + graph[depth], plus-1, minus, mul, div)
    
    if(minus != 0):
       
        dfs(depth+1, now - graph[depth], plus, minus-1, mul, div)

    if(mul != 0):
        
        dfs(depth+1, now * graph[depth], plus, minus, mul-1, div)

    if(div != 0):
        dfs(depth+1, int(now / graph[depth]), plus, minus, mul, div-1)




n = int(input())
graph = list(map(int, input().split()))
op = list(map(int, input().split()))

mn = int(1e9)
mx = -int(1e9)

dfs(1,graph[0], op[0], op[1], op[2], op[3])
print(mx)
print(mn)
