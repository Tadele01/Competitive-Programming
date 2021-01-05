def sortColors(arr):        
    for i in range(len(arr)):
        for j in range(i, -1, -1):
            if arr[i] < arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
                i -=1