import sys
input = sys.stdin.readline
from collections import deque


def balance(p):
    q = deque()
    for i in range(len(p)):
        if(p[i] == '('):
            q.append(p[i])
        else:
            if(not q):
                return False
            q.popleft()
                
    
    return True

def findu(p):
    ans = [0] * 2
    if(p[0] == '('):
        ans[0]+=1
    else:
        ans[1]+=1
    idx = 0
    for i in range(1,len(p)):
        if(p[i] == '('):
            ans[0]+=1
        else:
            ans[1]+=1
        if(ans[0] == ans[1]):
            idx = i
            break
    return idx






    




#두개 분리하기 올바른 문자열인지 여부, 인덱스 값 반환



def solution(p):
    if(len(p) == 0):
        return ""
    idx = findu(p)+1
    u = p[:idx]
    v = p[idx:]

    if(balance(u)):
        return u+solution(v)
        
    else:
        result = '('
        result+=solution(v)
        result += ')'
        
        u = u[1:-1]
        rs = ''
        for char in u:
            if(char == '('):
                rs+=')'
            else:
                rs+='('
        result += rs
        return result
p = input().rstrip()
ans = solution(p)
print(ans)


#문자열 문제에서는 리스트 append로 해결하려 하지 말고 더하기 연산으로 해결하기

        
    




