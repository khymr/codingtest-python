import sys
input = sys.stdin.readline

word = input().rstrip()

ans= []
sum = 0
for i in range(len(word)):
    if('0' <= word[i] <= '9'):
        sum += int(word[i])
        
    else:
        ans.append(word[i])
ans.sort()
ans.append(sum)
for i in range(len(ans)):
    print(ans[i], end = '')

