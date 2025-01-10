import sys
input = sys.stdin.readline

n,k = map(int, input().split())
lst_1 = list(map(int, input().split()))
lst_2 = list(map(int, input().split()))
lst_1.sort()
lst_2.sort(reverse=True)


for i in range(k):
    if(lst_1[i] < lst_2[i]):
        lst_1[i], lst_2[i] = lst_2[i], lst_1[i]
    else:
        break
print(sum(lst_1))

