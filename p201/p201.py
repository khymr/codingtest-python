import sys
input = sys.stdin.readline

result = 0

def binary_search(lst, start, end, result):
    if(start >= end): #꼭 똑같지 않을 수도 있고 이상 잘릴 수 있기 때문에 이렇게 조건을 걸어야한다
        print(result)
        return
    mid = (start + end) // 2
    total = 0
    for i in range(len(lst)-1, -1, -1):
        if(lst[i] <= mid):
            break
        total += (lst[i]- mid)

    if(total < m):
        return binary_search(lst, start, mid-1, result)
    else:
        result = mid
        return binary_search(lst, mid+1, end, result)
    



        

n,m = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

binary_search(lst, 1, max(lst), 0)
