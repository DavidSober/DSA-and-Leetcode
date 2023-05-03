# beats 10% in time and 5% in space
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        compare = root.val
        ans = True
        def dfs(node):
            nonlocal compare
            nonlocal ans
            if not node:
                return 

            if node.val != compare:
                ans = False 
            dfs(node.left)
            dfs(node.right)
            return 
        dfs(root)
        return ans
        