import sys
input = sys.stdin.readline
#이런 문제는 첫번쨰 시작 원소와 마지막 시작 원소를 동일한 함수에서 찾으려 하지말고
#first 함수, last함수 따로 작성해서 각각 구하기

# def binary_search(lst, start, end, target):
#     if(start > end):
#         return -1
#     mid = (start + end) //2

#     if(lst[mid] == target):
#         return mid
#     elif(lst[mid] > target):
#         return binary_search(lst, start, mid-1, target)
#     else:
#         return binary_search(lst, mid+1,end,target)

# n,x = map(int, input().split())

# lst = list(map(int, input().split()))

# idx = binary_search(lst, 0, len(lst)-1, x)

# if(idx == -1):
#     print(-1)
# else:
#     a = idx-1
#     b = idx+1
#     while(True):
#         if(lst[a] != lst[idx]):
#             break
#         a-=1
#     while(True):
#         if(lst[b] != lst[idx]):
#             break
#         b+=1
#     print(b-a-1)    

def first(graph, start, end, target):
    if(start > end):
        return -1
    mid = (start + end) // 2
    if(graph[mid] == target and graph[mid-1] < target):
        return mid
    elif(graph[mid] >= target):
        return first(graph, start, mid-1, target)
    else:
        return first(graph, mid+1, end, target)

def last(graph, start, end, target):
    if(start > end):
        return -1
    mid = (start + end) // 2
    if(graph[mid] == target and graph[mid+1] > target):
        return mid
    elif(graph[mid] > target):
        return last(graph, start, mid-1, target)
    else:
        return last(graph, mid+1, end, target)

    
           
n,x = map(int, input().split())
lst = list(map(int, input().split()))

e = len(lst)-1

f = first(lst, 0, e, x)
l = last(lst, 0, e, x)
if(f == -1 or l == -1):
    print(-1)
else:

    print(l-f+1)