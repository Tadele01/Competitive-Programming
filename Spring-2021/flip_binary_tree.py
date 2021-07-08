from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        ptr, stack, result = 0, [root], []
        while stack:
            cur_node = stack.pop()
            if cur_node.val != voyage[ptr]:
                return [-1]
            if cur_node.left and ptr+1 < len(voyage) and cur_node.left.val != voyage[ptr+1]:
                cur_node.left, cur_node.right = cur_node.right, cur_node.left
                result.append(cur_node.val)

            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)

            ptr += 1

        return result