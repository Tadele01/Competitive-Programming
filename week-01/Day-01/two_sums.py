'''
    in this we are given an array of integers and a target from the given array we return an indices which
    values are summed up to the target

    The naive approach is we pick an elt from the array add it with all other elts in the array step by step
    and compare the result with the target we'll do this for elts in the array if we found the two elements 
    which add up to target we will return the indices where this elts occured, 
    if we visit all elements in the array, but we don't find elts add up to target we'll return None



'''
class TwoSums:
    def two_sums(self, nums, target):
        hash_map = dict()
        for i in range(len(nums)):
            value = target - nums[i]
            if value in hash_map:
                arr = [i]
                arr.append(hash_map.get(value))
                return arr
            hash_map[nums[i]] = i
        return None


a = TwoSums()
z = a.two_sums([-1,-2,-3,-4,-5], -8)