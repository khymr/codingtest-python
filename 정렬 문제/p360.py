import sys
input = sys.stdin.readline

#짝수 개 있을 때 중간값이 2개이지만 2가지의 값은(거리) 일치하기 때문에 고려할 필요 없이 그냥 n-1을 2로 나눈 몫을 택일하면 된다 


# n = int(input())
# array = list(map(int, input().split()))

# array.sort()

# if(n % 2 == 0):
#     c = [n // 2 -1, n // 2]
    
#     distance =[0] * 2
#     for j in range(2):
#         for i in range(len(array)):
#             if(i != c[j]):
#                 distance[j] += (abs(array[i] - array[c[j]]))
#     if(distance[0] > distance[1]):
#         print(array[n // 2])
#     else:
#         print(array[n // 2 -1])        




# else:
#     print(array[n//2])

n = int(input())
array = list(map(int, input().split()))
array.sort()
print(array[(n-1)//2])
   
