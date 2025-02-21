import sys
input = sys.stdin.readline

def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result =[[0] * n for _ in range(m)] 
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result
def check(answer):
    lock_length = len(answer) // 3
    for i in range(lock_length, lock_length *2):
        for j in range(lock_length, lock_length *2):
            if(answer[i][j] != 1):
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    answer = [[0] * (n * 3) for _ in range(n * 3)]
   
    for i in range(n):
        for j in range(n):
            answer[i + n][j + n] = lock[i][j]
    for _ in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        answer[x + i][y + j] += key[i][j]
                if(check(answer) == True):
                    return True
                for i in range(m):
                    for j in range(m):
                        answer[x+i][y+j] -=key[i][j]
    return False
                


