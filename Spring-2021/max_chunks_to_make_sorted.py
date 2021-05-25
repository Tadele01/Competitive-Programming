class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        container = set()
        longest = 0
        for i in range(len(arr)):
            all_found = True
            for k in range(0, i):
                if k not in container:
                    all_found = False
                    
            if all_found:
                longest +=1
            
            container.add(arr[i])
        
        return longest
        