from typing import List
from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pairs = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    pairs[nums[i] + nums[j]].append((i, j))

        result, seen = set(), set()

        for pair_sum, index in pairs.items():
            if target - pair_sum in pairs:
                for idx1 in pairs[pair_sum]:
                    for idx2 in pairs[target-pair_sum]:
                        quad = tuple(sorted(list(set(list(idx1 + idx2)))))
                        if len(quad) == 4 and quad not in seen:
                            seen.add(quad)
                            indices = []
                            for i in idx1:
                                indices.append(nums[i])
                            for i in idx2:
                                indices.append(nums[i])
                            indices = tuple(sorted(indices))
                            result.add(indices)

        return result
     