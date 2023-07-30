# beats 87% in time and 11% in space

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return

            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.val == 0:
                return False
            elif node.val == 1:
                return True

            if node.val == 2:
                return left or right
            elif node.val == 3:
                return left and right
        return dfs(root)