# beats 75% in time and 65% in space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            temp = node.val # store val in temp first
            node.val = abs(left - right) # then change node.val as required by question
            ans.append(node.val)

            return temp + left + right# return prev store node.val for future calc

        dfs(root)
        print(ans)
        return sum(ans)
