# beats 25% in time and 12% in space
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sums = []
        def dfs(node):
            if not node:
                return 0 
 
            left = dfs(node.left)
            right = dfs(node.right)   
            
            sums.append(node.val + left + right)
            return left + right + node.val

        dfs(root)
        counts = Counter(sums)
        mx = float('-inf') # max freq in sums
        for key in counts:
            if mx < counts[key]:
                mx = counts[key]
        ans = []
        for key in counts:
            if counts[key] == mx:
                ans.append(key)
        return ans

        
        
        