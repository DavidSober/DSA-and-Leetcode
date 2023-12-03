# beats 5% in time and 6% in space

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        def dfs(node):
            if not node:
                return 
            
            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return vals