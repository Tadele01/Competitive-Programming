def counting_sort(arr):
    '''
        In counting sort we pick the max element from the array and build a max+1 range array
        for storing how many times each element is repeated then from it we can build a sorted
        version of our array 

        its running time is O(n + k) where k is the larges number in the given array
        its space complexity is O(n) because we used additional memory
    '''
    max_ = arr[0]
    min_ = arr[0]
    for elt in arr:
        if elt > max_:
            max_ = elt
        if elt < min_:
            min_ = elt
    collector = []
    for i in range(min_, max_+1):
        collector.append(0)

    for elt in arr:
        collector[elt] +=1
    sorted_arr = []
    
    for i in range(len(collector)):
        for j in range(collector[i]):
            sorted_arr.append(i)

    return sorted_arr
