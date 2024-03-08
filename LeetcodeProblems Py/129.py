# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        paths = []
        currpath = []
        def dfs(node):
            if not node:
                return
            print(currpath)
            if node.left == None and node.right == None:
                currpath.append(node.val)
                paths.append(currpath.copy())
                currpath.pop()
            currpath.append(node.val)
            dfs(node.left)
            dfs(node.right)
            currpath.pop()
        dfs(root)
        ans = 0
        print(paths)
        for path in paths:
            lst = ""
            for num in path:
                lst += str(num)
            ans += int(lst)
        return ans