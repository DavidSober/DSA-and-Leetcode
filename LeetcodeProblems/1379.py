# beats 36% in time and 8% in space

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ref = 0
        def dfs(node):
            nonlocal ref
            if not node:
                return 
            
            if node.val == target.val:
                ref = node 

            dfs(node.left)
            dfs(node.right)
            return 
        dfs(cloned)
        return ref

