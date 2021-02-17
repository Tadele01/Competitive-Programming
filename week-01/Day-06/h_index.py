class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        h_index = 0
        N = len(citations) 
        for h in range(N+1):
            count = 0
            for value in citations:
                if value >= h:
                    count +=1
            if count >= h:
                count = 0
                N_h = N - h
                for value in citations:
                    if value <= h:
                        count +=1
                if count >= N_h and h > h_index:
                    h_index = h
        return h_index
                    