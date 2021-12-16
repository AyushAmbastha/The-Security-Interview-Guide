# Take one element from 1: and insert in the correct position. 

arr = [34,56,7,87,23]

for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
    arr[j + 1] = key
 
print(arr)