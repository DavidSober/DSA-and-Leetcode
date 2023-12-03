# beats 20% in time and 6% in space
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            dfs(node.right)
            vals.append(node.val)
            return 
        dfs(root)
        return vals
            