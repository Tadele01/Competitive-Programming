class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        res, hash_map = set(), {}
        container = defaultdict(int)
        def adder(name, i):
            if name not in res:
                res.add(name)
                hash_map[i] = name
                container[name] = 0
            else:
                while name in res:
                    name = names[i]
                    index = container[name]
                    container[name] = index +1
                    name += '(' + str(index+1) + ')'
                res.add(name)
                hash_map[i] = name
                
        for i in range(len(names)):
            adder(names[i], i)
            
        return hash_map.values()