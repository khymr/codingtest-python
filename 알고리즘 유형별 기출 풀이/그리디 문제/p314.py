import sys
input = sys.stdin.readline
# INF = int(1e9)
# n = int(input())
# ans = [0] * INF
# array = set([])
# coin = list(map(int, input().split()))

# coin.sort()
# print(coin)
# for c in coin:
#    ln = len(array)
#    for i in range(ln):
#       array.add(array[i]+c)      
#    array.add(c)
# for i in range(1,len(ans)):
#    if(i not in array):
#       print(i)
#       break
#이문제는 하나하나 set에 넣어서 문제 답을 얻어가기 보다는 target값 설정하고 값이 있는지 여부를 찾아보는 방식으로 풀기   

n = int(input())
coin = list(map(int, input().split()))    
coin.sort()

target = 1
for c in coin:
    if(c > target):
        break
    target += c
print(target)