def counting_sort(arr):
    '''
        In counting sort we pick the max element from the array and build a max+1 range array
        for storing how many times each element is repeated then from it we can build a sorted
        version of our array 

        its running time is O(n + k) where k is the larges number in the given array
        its space complexity is O(n) because we used additional memory

        when it comes to negative numbers my initial thought is to keep them in separate array
        
    '''
    min_ = arr[0]
    max_ = arr[0]
    for elt in arr:
        if elt < min_:
            min_ = elt
        if elt > max_:
            max_ = elt
    count_arr = [0] * (abs(min_)+abs(max_) + 1)
    for elt in arr:
        index = elt - min_
        count_arr[index] +=1
    sorted_arr = []
    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
            sorted_arr.append(i+min_)
    return sorted_arr
print(counting_sort([-1, -1, -39, 0, 9]))