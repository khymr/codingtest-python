import sys
input = sys.stdin.readline


n = int(input())
lst = []
for _ in range(n):
    name, grade = input().split()
    # lst.append((int(grade), name))
    lst.append((name, int(grade)))
lst.sort(key = lambda x : x[1])
for i in lst:
    print(i[0], end = ' ')
#정렬 순서 정하기 귀찮으면 그냥 제일 첫번째 원소에 정렬해야할 원소 놓기. 만약 정렬을 여러 기준으로 해아하면 lambda 사용
