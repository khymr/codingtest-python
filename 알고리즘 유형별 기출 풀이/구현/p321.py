import sys
input = sys.stdin.readline

n = int(input())
ans = n

cnt =0
while(n > 0):
    cnt+=1
    n //=10
sum1 = 0
sum2 = 0
for i in range(cnt):
    elem = ans % 10
    if(i < cnt // 2):
        sum1 += elem
    else:
        sum2 += elem
    ans //=10
if(sum1 == sum2):
    print("LUCKY")
else:
    print("READY")