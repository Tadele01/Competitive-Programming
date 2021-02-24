class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        push = ["Push"]
        pop = ["Push", "Pop"]
        
        for i in range(1, target[-1]+1):
            if i in target:
                stack.extend(push)
            else: 
                stack.extend(pop)
                
        return stack