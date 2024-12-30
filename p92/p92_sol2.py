import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort(reverse=True)

first = lst[0]
second = lst[1]

count = (m //(k+1)) * k  #int(m / (k+1)) * k
count += m % (k+1)

tot = first * (count) + second *(m-count)
print(tot)