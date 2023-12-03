# beats 6% in time and 38% in space
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        pathS = []
        path = []
        def dfs(node):
            if not node:
                return 
            path.append(node.val)
            if node.left == None and node.right == None:
                pathS.append(path.copy())

            dfs(node.left)
            dfs(node.right)

            path.pop() # as we go back up the tree we need to pop values
            return 
        dfs(root)
        ans = []
        for path in pathS:
            if sum(path) == targetSum:
                ans.append(path)
        
        return ans