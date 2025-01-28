import sys
input = sys.stdin.readline
#많이 어려웠던 문제-> while문으로 푸는게 더 편하다는데 나는 개인적으로 재귀로만 bs를 풀었어서 재귀로 품 이문제도


def isGap(graph, c, mid):
    count = 1
    last_install = graph[0]
    for i in range(1,len(graph)):
        if(graph[i] - last_install >= mid):
            count += 1
            last_install = graph[i]
    if(count >= c):
        return True
    return False

def binary_search(graph, start, end, result):
    if(start > end):
        return result
    mid = (start + end) // 2
    if(isGap(graph, c, mid)):
        return binary_search(graph, mid+1, end, mid)
    else:
        return binary_search(graph, start , mid-1, result)

n,c = map(int, input().split())
lst= []
for _ in range(n):
    lst.append(int(input()))
lst.sort()
start = 1
end = lst[-1] - lst[0]

result = 0

ans = binary_search(lst, start , end, result)
print(ans)
