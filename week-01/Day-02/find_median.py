def findMedian(arr):
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
    median = len(sorted_arr) //2
    return sorted_arr[median]