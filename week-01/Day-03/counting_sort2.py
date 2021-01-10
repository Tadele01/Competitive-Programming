def countingSort(arr):
    '''
       counting sort is basically create a count array with range min, max
       where min and max are the minimum and the maximum elements of the given array
       then for each element in the array increment elements in the count array if 
       they occur in the original given array 
       
       
    '''
    max_ = arr[0]
    min_ = arr[0]
    for elt in arr:
        if elt < min_:
            min_ = elt
        if elt > max_:
            max_ = elt
    count = [0] * (max_+1) #since we need to include the max element
    for elt in arr:
        count[elt] += 1
    sorted_arr = []
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_arr.append(i)
    return sorted_arr