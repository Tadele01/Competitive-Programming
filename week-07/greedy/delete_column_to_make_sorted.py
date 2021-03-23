class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        length, count = len(strs[0]), 0
        for i in range(length):
            for j in range(1, len(strs)):
                if strs[j][i] < strs[j-1][i]:
                    count +=1 
                    break
        return count
                