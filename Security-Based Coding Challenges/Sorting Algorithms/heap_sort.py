def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    print('inital largest', largest)
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r
        
    print(largest, '-', l, '-', r, 'a[i]', arr[i])

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    #Build max heap
    for i in range(n//2,-1,-1):
        heapify(arr, n, i)

    #Send largest element, which is on the top after heapify, to the end (swap with first element)
    #Remove it from the heap, by sending n-1 as lenght of array. and saying fix from i=0, where you made a change.
    for i in range(n-1, 0, -1):
          # Swap
          arr[i], arr[0] = arr[0], arr[i]
  
          # Heapify root element
          heapify(arr, i, 0)


arr = [1, 12, 9, 5, 6, 10]
heapSort(arr)
print(arr)