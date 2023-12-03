# beats 40% in time and 93% in space


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node):
            nonlocal ans
            if not node:
                return

            left = dfs(node.left)
            ans.append(node.val)
            right = dfs(node.right)
            
        dfs(root)
        return ans