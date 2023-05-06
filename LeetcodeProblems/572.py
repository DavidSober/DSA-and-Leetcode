# Serialization of the tree paths
# this approach works and is good to know but there might be a more simple one
# beats 92% in time and 6% in space
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        path = []
        def dfs(node): # first dfs in order for the subroot 
            if not node:
                return 
            path.append(' ')
            path.append(node.val)
            if node.left == None:
                path.append('#')
            dfs(node.left)
            if node.right == None:
                path.append('#')
            dfs(node.right)
            return 
        dfs(subRoot)
        subpath = path.copy()
        path = []
        dfs(root)
        
        def strmaker(nums):
            ret = ''
            for i in nums:
                ret += str(i) + ','
            return ret
        subpathSTR = strmaker(subpath)
        pathSTR = strmaker(path)
        # print(subpathSTR, pathSTR)
        if subpathSTR in pathSTR:
            return True
        else:
            return False