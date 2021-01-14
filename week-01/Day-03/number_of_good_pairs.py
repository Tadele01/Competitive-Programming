def numIdenticalPairs(nums):
    good_num = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and i<j:
                good_num +=1
    return good_num