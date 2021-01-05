
def selection_sort(arr):
    '''
        -selection sort work the same way as bubble sort works but in selection sort for each iteration we
        pick a minimum element and put it on the right spot in this case we gurantee the minimum value be at its
        appropirate position
    '''
    for i in range(len(arr)):
        min_ = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min_:
                tmp = arr[j]
                arr[j] = min_
                arr[i] = tmp
    return arr
