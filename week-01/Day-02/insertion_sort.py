def insertion_sort(arr):
    '''
        - in insertion sort we iterate though the array, compare the current element to its predeccsor
            if: the current is smaller compare it the element before ...
        
        it is in place sorting algorithm and also it can be implemented to be a stable
    '''

    for i in range(len(arr)):
        for j in range(i, -1, -1):
            if arr[i] < arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
                i -=1
    return arr