array = [5,7,9,0,3,1,6,2,4,8]

# def quick_sort(array, start, end):
#     if(start >= end):
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while(left <= right):
#         while(left <= end and array[pivot] >= array[left]): # 끝까지 탐색 가능
#             left +=1
#         while(right > start and array[pivot] <= array[right]): #피벗 보다 1큰 곳 까지 탐색가능
#             right-=1
#         if(left > right): #엇갈렸을 때 교체 작업 진행
#             array[pivot], array[right] = array[right], array[pivot]
            
#         else:
#             array[left], array[right] = array[right], array[left]
        
#     quick_sort(array, start, right-1)
#     quick_sort(array, right+1, end)


# quick_sort(array, 0, len(array)-1)
# print(array)


def quick_sort(array, start , end):
    if(start >= end):
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left +=1
        while(right > start and array[right] >= array[pivot]):
            right-=1
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left],array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

    



quick_sort(array, 0, len(array)-1)
print(array)