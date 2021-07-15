from collections import defaultdict
from typing import List
class Hierarchy:
    def __init__(self, name):
        self.root = Node(name)
        self.hierarchy = defaultdict(list)
        self.people = {name:self.root}
        
    def inheritance(self):
        result = []
        root = self.root
        self.dfs(root, result)
        return result

    def dfs(self, root, result):
        if not root.is_dead:
            result.append(root.name)
        for child in self.hierarchy[root.name]:
            self.dfs(child, result)
            
class Node:
    def __init__(self, name):
        self.name = name
        self.is_dead = False
    
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Hierarchy(kingName)
        
    def birth(self, parentName: str, childName: str) -> None:
        new_child = Node(childName)
        self.root.hierarchy[parentName].append(new_child)
        self.root.people[childName] = new_child

    def death(self, name: str) -> None:
        self.root.people[name].is_dead = True
        
    def getInheritanceOrder(self) -> List[str]:
        return self.root.inheritance()