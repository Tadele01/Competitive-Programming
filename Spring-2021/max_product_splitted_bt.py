class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        memo = {}
        node_collector = []
        tot_sum = self.dfs(root, memo)
        max_prod = 0
        self.node_collector(root, node_collector)
        for node in node_collector:
            sum_node = self.dfs(node, memo)
            diff = tot_sum - sum_node
            max_prod = max(max_prod, diff * sum_node)
        return max_prod % (10**9 + 7)
    
    def node_collector(self, root, node_collector):
        if not root:
            return 0
        node_collector.append(root)
        self.node_collector(root.left, node_collector)
        self.node_collector(root.right, node_collector)
        
    def dfs(self, root, memo):
        if not root:
            return 0
        if root in memo:
            return memo[root]
        left, right = self.dfs(root.left, memo), self.dfs(root.right, memo)
        memo[root] = root.val + left + right
        return memo[root]
        
        