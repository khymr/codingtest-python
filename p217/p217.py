import sys
input = sys.stdin.readline
n = int(input())

array = [0] * (n+1)


for i in range(2,n+1):
    array[i] = array[i-1] + 1
    if(i % 2 == 0):
        array[i] = min(array[i], array[i//2] + 1)
    if(i % 3 == 0):
        array[i] = min(array[i], array[i//3] + 1)
    if(i % 5 == 0):
        array[i] = min(array[i], array[i//5] + 1)
    

print(array[n])
    