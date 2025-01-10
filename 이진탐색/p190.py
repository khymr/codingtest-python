import sys
input = sys.stdin.readline

def binary_search(lst, start , end):
    if(start > end):
        return None # None을 파이썬에서는 쓴다 기억해두기
    mid = (start + end) // 2
    if(lst[mid] == ans):
        return mid + 1
    elif(lst[mid] > ans):
        return binary_search(lst, start, mid-1)
    else:
        return binary_search(lst, mid + 1, end)




n, ans = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

idx = binary_search(lst, 0, len(lst)-1)
print(idx)

