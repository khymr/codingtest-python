import sys
input = sys.stdin.readline

n = int(input())

array = [0] * (n)
array[0] = 1
array[1] = 3

for i in range(2, n):
    array[i] = (array[i-2] * 2 + array[i-1]) % 796796


print(array[n-1]) 