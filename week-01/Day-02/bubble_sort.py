def bubble_sort(arr):
    '''
        A bubble sort is a sorting algorithm for each iteration it will bubble the largest element
        from the array to its appropirate position 

        -It hava a running time of O(n^2)
        -It is in-place sort
        -It can be implemented to be a stable sorting algorithm
    '''

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr

print(bubble_sort([4, 5, 6, 12, 12, -1, 0]))