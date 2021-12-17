#Iterate through each element pretty much. Swap adjacent elements in the array
#Largest elements is being sent to the end each iteration of i

list = [34,56,7,87,23]

for i in range(len(list)-1):
    for j in range(len(list)-1-i):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

print(list)