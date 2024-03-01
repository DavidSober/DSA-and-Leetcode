# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        depth = 0
        ans = root.val
        maxD = 0
        def dfs(node):
            nonlocal maxD
            nonlocal ans
            nonlocal depth
            if not node:
                return
            depth += 1
            if node.left == None and node.right == None:
                if depth > maxD:
                    maxD = depth
                    ans = node.val

            dfs(node.left)
            dfs(node.right)

            depth -= 1
        dfs(root)
        return ans