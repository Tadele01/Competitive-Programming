class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        x, y = 1, z
        pairs = []
        while x<=z and y>0:
            f = customfunction.f(x,y)
            if f==z:
                pairs.append([x,y])
                x, y = x+1, y-1
            elif f > z:
                y -= 1
            else:
                x += 1
        return pairs