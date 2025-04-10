import sys
input = sys.stdin.readline
from itertools import combinations

def calculate(prev, op, next):
    
    if(op == '+'):
        return prev + next
    elif(op == '-'):
        return prev - next
    elif(op == '*'):
        return prev * next



def operation(operation_idx_lst, s):
    s = list(s)
    for i in range(n):
        if(i % 2 == 0):
            s[i] = int(s[i])
    
    new_arr = []
    i = 0
    while(i < n):
        if(i not in operation_idx_lst):
            new_arr.append(s[i])
            i+=1
        else:
            prev = new_arr.pop()
            op = s[i]
            next = s[i+1]
            rs = calculate(prev, op, next)
            new_arr.append(rs)
            i+=2
    result = new_arr[0]
    for i in range(1,len(new_arr),2):
        result = calculate(result, new_arr[i], new_arr[i+1])
    return result


        
        



n = int(input())
s = input().rstrip()

operation_list = [i for i in range(1,n,2)]
max_rs = float('-inf')

for i in range(len(operation_list)+1):
    comb = list(combinations(operation_list,i))

    for c in comb:
        rs = 0
        if(len(c)>1):
            gOrStop = 0
            for j in range(len(c)-1):
                if(c[j] + 2 == c[j+1]):
                    gOrStop = 1
                    break
            if(gOrStop == 1):
                continue
            rs = operation(c, s)
            if(rs > max_rs):
                max_rs = rs
        else:
            rs = operation(c, s)
            if(rs > max_rs):
                max_rs = rs
print(max_rs)





