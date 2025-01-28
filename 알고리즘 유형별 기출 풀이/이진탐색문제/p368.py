import sys
input = sys.stdin.readline

def binary_search(arr,start, end):
    if(start > end):
        return -1
    mid = (start + end) //2

    if(mid == arr[mid]):
        return mid
    elif(mid < arr[mid]):
        return binary_search(arr, start, mid-1)
    else:
        return binary_search(arr, mid+1, end)

n = int(input())

arr = list(map(int, input().split()))

rs = binary_search(arr, 0, len(arr)-1)
print(rs)