from typing import List
class Solution:
    def h_indexII(self, citations:List)->int:
        h_index = 0
        index = 0
        for i in range(len(citations)-1, -1, -1):
            if citations[i] > index:
                h_index +=1
            index +=1
        return h_index
