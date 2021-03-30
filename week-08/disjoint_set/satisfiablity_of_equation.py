class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        leaders = [i for i  in range(26)]
        size = [1 for i in range(26)]
        def find(x):
            if leaders[x] == x:
                return leaders[x]
            leaders[x] = find(leaders[x])
            return leaders[x]
        
        def union(x, y):
            x_lead, y_lead = find(x), find(y)
            if size[x_lead] > size[y_lead]:
                leaders[y_lead] = x_lead
                size[x_lead] += size[y_lead]
            elif size[y_lead] >= size[x_lead]:
                leaders[x_lead] = y_lead
                size[y_lead] += size[x_lead]
            
        for eqn in equations:
            x, y = ord(eqn[0]) - ord('a'), ord(eqn[-1]) - ord('a')
            if eqn[1] == '=':
                union(x, y)
        
        for eqn in equations:
            x, y = ord(eqn[0]) - ord('a'), ord(eqn[-1]) - ord('a')
            if eqn[1] == '!' and find(x) == find(y) :
                return False
        
        return True
                
        
        