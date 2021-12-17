#Find the min element in the array and put at beginning and then do same from 1: and then 2: ...

list = [34,56,7,87,23]

for i in range(len(list)):
    min_ind = i
    for j in range(i+1,len(list)):
        if list[j] < list[min_ind]:
            min_ind=j
        
    list[min_ind], list[i] = list[i], list[min_ind]

print(list)