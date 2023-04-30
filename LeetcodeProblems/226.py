# beats 66% in time and 8.5% in space why is space not great?
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return 
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            node.left, node.right = node.right, node.left
            
            return left and right
        dfs(root)
        return root 