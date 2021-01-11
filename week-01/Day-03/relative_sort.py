def relativeSortArray(arr1, arr2):
    max_ = max(arr1)
    count = [0] * (max_ + 1)
    for elt in arr1:
        count[elt] += 1
    all_sort = []
    for elt in arr2:
        for i in range(count[elt]):
            all_sort.append(elt)
            arr1.remove(elt)
    if arr1:
        left_overs = []
        max_ = max(arr1)
        count = [0] * (max_ + 1)
        for elt in arr1:
            count[elt] += 1
        for i in range(len(count)):
            for j in range(count[i]):
                left_overs.append(i)
        all_sort.extend(left_overs)
    return all_sort
print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))