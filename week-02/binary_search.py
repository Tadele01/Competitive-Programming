def search(nums, target):
    index = 0
    while True:
        middle = len(nums) // 2
        index += middle
        if nums[middle] == target:
            return index
        elif nums[middle] > target:
            nums = nums[:middle]
        elif nums[middle] < target:
            nums = nums[middle:]
        if len(nums) == 1:
            middle = len(nums) // 2
            if nums[middle] == target:
                return index
        else:
            break

        
        
    return - 1
print(search([-1,0,3,5,9,12], 2))