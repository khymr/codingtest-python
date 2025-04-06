import sys
from collections import deque

input = sys.stdin.readline
mountain = []
def binary_search(height):
    idx = len(mountain)
    left, right = 0, len(mountain) - 1

    while left <= right:
        mid = (left + right) // 2
        min_item = mountain[mid][-1]  # peekLast
        if min_item < height:
            left = mid + 1
        else:
            idx = mid
            right = mid - 1
    return idx

Q = int(input())
stack = []


for _ in range(Q):
    parts = list(map(int, input().split()))
    command = parts[0]

    if command == 100:
        for i in range(2, len(parts)):
            height = parts[i]
            idx = binary_search(height) if mountain else 0
            stack.append(idx)
            if idx == len(mountain):
                mountain.append(deque())
            mountain[idx].append(height)

    elif command == 200:
        height = int(parts[1])
        idx = binary_search(height) if mountain else 0
        stack.append(idx)
        if idx == len(mountain):
            mountain.append(deque())
        mountain[idx].append(height)
        N += 1

    elif command == 300:
        last_idx = stack.pop()
        mountain[last_idx].pop()
        if not mountain[last_idx]:
            mountain.pop(last_idx)
        N -= 1

    elif command == 400:
        m_index = int(parts[1]) - 1
        cable_climb = stack[m_index]
        max_climb = len(mountain) - 1
        max_height = mountain[-1][0]  # peekFirst
        point = (cable_climb + len(mountain)) * 1000000 + max_height
        print(point)