# beats 20% in time and 90% in space 

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans  
            if not node:
                return [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val == (left[0] + right[0] + node.val) // (left[1] + right[1] + 1):
                ans += 1 

            return [left[0] + right[0] + node.val, left[1] + right[1] + 1]
        dfs(root)
        return ans