import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort(reverse=True)
cnt = 0
sum =0
for i in range(m):
    
    if(cnt == k):
        cnt = 0
        sum += lst[1]
        continue
    cnt+=1
    sum+=lst[0]

print(sum)


