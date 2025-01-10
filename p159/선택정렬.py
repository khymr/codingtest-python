import sys
input = sys.stdin.readline

array = [7,5,9,0,3,1,6,2,4,8]
for i in range(0,len(array)-1):
    min = array[i]
    idx = i
    for j in range(i+1, len(array)):
        if(min > array[j]):
            min = array[j]
            idx = j
    if(i != idx):
        array[idx], array[i] = array[i], array[idx]
print(array)
        
    