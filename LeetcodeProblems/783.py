# beats 14% in time and 32% in space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        order = []
        def dfs(node):
            nonlocal order
            if not node:
                return 
            
            dfs(node.left)
            order.append(node.val)
            dfs(node.right)

        dfs(root)
        print(order)
        smallDelta = float('inf')
        for i in range(len(order) - 1):
            if order[i + 1] - order[i] < smallDelta:
                smallDelta = order[i + 1] - order[i]
        return smallDelta
