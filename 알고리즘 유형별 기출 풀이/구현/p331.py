import sys
input = sys.stdin.readline

def possible(result):
    for x,y,a in result:
        if(a == 0):#기둥
            if(y == 0 or [x-1, y,1] in result or [x,y,1] in result or [x,y-1,0] in result):
                continue
            else:
                return False
        else:
            if([x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y,1] in result and 
                                                                [x+1,y,1] in result)):
                continue
            else:

                return False
    return True







def solution(n, build_frame):
    result = []
    for bf in build_frame:
        x,y,a,b = bf
        if(b == 0):
            result.remove([x,y,a])

            if(possible(result)):
                continue
            else:
                result.append([x,y,a])
        else:
            result.append([x,y,a])
            if(possible(result)):
                continue
            else:
                result.remove([x,y,a])
    result.sort()
    return result
            
        
        


n = int(input())
array = [[-1] * (n+1) for _ in range(n+1)]
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
rs = solution(n, build_frame)
print(rs)