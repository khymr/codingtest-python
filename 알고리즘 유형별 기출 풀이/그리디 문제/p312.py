import sys
input = sys.stdin.readline

array = input().rstrip()

prev = int(array[0])
for i in range(1,len(array)):
    next = int(array[i])
    if(prev == 0 or prev == 1 or next == 0 or next == 1): # 실제로는 <=1 이렇게만 하면 된다
        prev = prev + next
    else:
        prev = prev * next
print(prev)
