class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        h_index = 0 
        for i, cite in enumerate(citations):
            if cite > i:
                h_index +=1
        return h_index
