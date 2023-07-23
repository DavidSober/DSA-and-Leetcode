# note this method of max_path_sum is less readable but faster than previous method  
# same time and space as below but better theoretical time comp

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path = []
        max_path_sum = 0
        ans = 0
        def dfs(node):
            nonlocal ans
            nonlocal max_path_sum
            if not node:
                return 
            path.append(node.val)
            max_path_sum += path[-1] 
            path_sum = max_path_sum 
            for i in range(len(path)):
                if path_sum == targetSum:
                    ans += 1
                path_sum -= path[i]
            dfs(node.left)
            dfs(node.right)
            max_path_sum -= path.pop()
        dfs(root)
        return ans


# this was my first attempt took 21 mins and is more readable than the above attempt but more slow
# beats 48% in time and 72% in space

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path = []
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 
            path.append(node.val)
            path_sum = sum(path) # could have path some as an int for optimization
            for i in range(len(path)):
                if path_sum == targetSum:
                    ans += 1
                path_sum -= path[i]
            dfs(node.left)
            dfs(node.right)
            path.pop()
        dfs(root)
        return ans