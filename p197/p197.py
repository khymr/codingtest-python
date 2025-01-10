import sys
input = sys.stdin.readline

def binary_search(lst, start, end, ans):
    if(start > end):
        return None
    mid = (start + end)//2
    if(lst[mid] == ans):
        return mid
    elif(lst[mid] > ans):
        return binary_search(lst, start, mid-1,ans)
    else:
        return binary_search(lst, mid +1, end, ans)
    

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

m = int(input())
ans = list(map(int, input().split()))

for a in ans:
    rs = binary_search(lst, 0, len(lst)-1, a)
    if(rs != None):
        print("yes", end = ' ')
    else:
        print("no", end = ' ')
