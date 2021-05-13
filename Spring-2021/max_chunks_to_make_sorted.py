class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        chunk_starts = set([0])
        self.chunk_creator(arr, 0, len(arr), chunk_starts)
        
        return len(chunk_starts)
        
    def chunk_creator(self, arr, start, end, chunk_starts):
        
        max_elt  = arr[start]
        
        for i in range(start, end):
            if i < len(arr) and arr[i] > max_elt and max(arr[start:i]) < min(arr[i:end+1]):
                chunk_starts.add(i)
                self.chunk_creator(arr, start, i, chunk_starts)
                self.chunk_creator(arr, i, end, chunk_starts)
                break

        
        