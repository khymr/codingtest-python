import sys
input = sys.stdin.readline

#내 코드 -> 틀림
# n = int(input())
# array = list(map(int, input().split()))

# array.sort(reverse=True)
# cnt = 0
# idx = 0
# while(idx <= len(array)-1):
#     elem = array[idx]
#     idx += elem
#     cnt+=1
# print(cnt)

#모범답안 코드
n = int(input())

array = list(map(int, input().split()))

array.sort()
cnt = 0
result = 0
for a in array:
    cnt+=1
    if(cnt >= a):
        cnt = 0
        result +=1
print(result)       


