def binary_search(arr, target, index=0):
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2
    index += mid
    if arr:
        if arr[mid] == target:
            return index
        elif arr[mid] > target:
            index -= mid
            arr = arr[:mid] 
            return binary_search(arr, target, index=index)
        elif arr[mid] < target:
            arr = arr[mid+1:]
            index += 1
            return binary_search(arr, target, index=index)
    return -1 #we return -1 if there is no element equals to the targe in the given array
print(binary_search([-1,0,3,5,9,12], -2))
