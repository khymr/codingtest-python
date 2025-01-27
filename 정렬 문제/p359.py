import sys
input = sys.stdin.readline

n = int(input())

student = []
for _ in range(n):
    name, read, eng, math = map(str, input().split())
    student.append((name, int(read), int(eng), int(math)))

student.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
for s in student:
    print(s[0])
