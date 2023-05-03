# beats 7% in time and 9% in space
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        vals = []
        def dfs(node):
            if not node:
                return 

            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

            return 
        dfs(root)
        minval = min(vals)
        while minval in vals:
            vals.remove(minval)
        if vals:
            return min(vals)
        else:
            return -1