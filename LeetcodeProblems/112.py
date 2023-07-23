# beats 61% in time and 81% in space
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path_sum = 0
        found = False
        def dfs(node):
            nonlocal path_sum
            nonlocal targetSum
            nonlocal found
            if not node or found == True:
                return 
            path_sum += node.val
            if path_sum == targetSum and node.left == None and node.right == None:
                found = True
            dfs(node.left)
            dfs(node.right)
            path_sum -= node.val

        dfs(root)
        return found