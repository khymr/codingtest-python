import sys
input = sys.stdin.readline
from collections import deque
locate = [(0,1), (1,0), (0,-1), (-1,0)]
def makeTrigger(trigger):
    if(trigger < 0):
        trigger = 3
    if(trigger > 3):
        trigger = 0
    return trigger
def solution(trigger):
    x = 1
    y = 1
    array[x][y] = 2
    cnt = 0
    q = deque()
    q.append((x,y))
    while(True):
        x += locate[trigger][0]
        y += locate[trigger][1]
        
        if(x < 1 or x > n or y < 1 or y > n or array[x][y] == 2):
            cnt+=1
            break
        if(array[x][y] == 0):
            array[x][y]=2
            q.append((x,y))
            px, py = q.popleft()
            array[px][py] = 0
            
        if(array[x][y] == 1):
            array[x][y] = 2
            q.append((x,y))
        cnt+=1
        if(rotate[cnt]!= False):
            if(rotate[cnt] == 'D'):
                trigger+=1
                
            else:
                trigger-=1
            trigger=makeTrigger(trigger)
    return cnt

        

            
        







n = int(input())
array = [[0] * (n+1) for _ in range(n+1)]



k = int(input())
for _ in range(k):
    x,y = map(int, input().split())
    array[x][y] = 1
l = int(input())
rotate = [False] * 10001
for _ in range(l):
    a,b = map(str, input().split())
    tm = int(a)
    rotate[tm] = b
trigger = 0
ans = solution(trigger)
print(ans)


    
    




