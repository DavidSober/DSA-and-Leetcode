# beats 51% in time and 83% in space
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left + right == node.val:
                ans += 1

            return node.val + left + right
        dfs(root)
        return ans