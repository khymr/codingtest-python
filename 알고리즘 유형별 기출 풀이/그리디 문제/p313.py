import sys
input = sys.stdin.readline

# array = input().rstrip()

# cnt = [0] * 2
# elem = array[0]
# for i in range(1,len(array)):
#     if(elem != array[i]):
#         cnt[int(elem)]+=1
#         elem = array[i]
#     else:
#         continue


# if(cnt[0] != 0 and cnt[1] != 0):
#     cnt[int(array[i])] +=1
# if(cnt[0] == 0 or cnt[1] == 0):
#     rs = max(cnt[0], cnt[1])
# else:

#     rs = min(cnt[0], cnt[1])
# print(rs)


#맞추긴 했는데 더 쉬운 방안 강구해보기


array = input().rstrip()

ans = [0] * 2
print(ans)
prev = array[0]

for i in range(1,len(array)):
    if(prev != array[i]):
        ans[int(prev)] +=1
        prev = array[i]
ans[int(prev)]+=1
print(min(ans))