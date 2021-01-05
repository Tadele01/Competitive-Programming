def counting_sort(arr):
    '''
        In counting sort we pick the max element from the array and build a max+1 range array
        for storing how many times each element is repeated then from it we can build a sorted
        version of our array 

        its running time is O(n + k) where k is the larges number in the given array
        its space complexity is O(n) because we used additional memory

        when it comes to negative numbers my initial thought is to keep them in separate array
        
    '''
    max_postive = arr[0]
    min_postive = arr[0]
    max_negative = -1
    min_negative = -10000
    for elt in arr:
        if elt >=0:
            if elt > max_postive:
                max_postive = elt
            if elt < min_postive:
                min_postive = elt
    for elt in arr:
        if elt <0:
            if elt > max_negative:
                max_negative = elt
            if elt < min_negative:
                min_negative = elt
    collector = []
    negative_collector = []
    min_negative = abs(min_negative)
    max_negative = abs(max_negative)
    for i in range(max_negative, min_negative):
        negative_collector.append(0)
    for i in range(min_postive, max_postive+1):
        collector.append(0)
    for elt in arr:
        if elt < 0:
            negative_collector[abs(elt)] +=1
    negative_sorted = []
    for i in range(len(negative_collector)):
        for j in range(negative_collector[i]):
            data = -1 * i
            negative_sorted.append(data)
    for elt in arr:
        if elt >=0:
            collector[elt] +=1
    sorted_arr = []
    
    for i in range(len(collector)):
        for j in range(collector[i]):
            sorted_arr.append(i)
    negative_sorted.extend(sorted_arr)
    sorted_arr = negative_sorted
    return sorted_arr

print(counting_sort([-1, -1, -39, 0, 9]))