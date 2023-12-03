# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)
        dfs(root)
        F = Counter(lst)
        lst = list(set(lst))
        lst = sorted(lst, key = lambda x: -F[x])
        most = F[lst[0]]
        ans = []
        for num in lst:
            if F[num] == most:
                ans.append(num)
        return ans