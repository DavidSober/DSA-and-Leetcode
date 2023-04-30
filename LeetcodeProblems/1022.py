# beats about 5% in time and space... could be better 
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        paths = []
        currpath = []
        def dfs(node):
            nonlocal paths
            nonlocal currpath
            if not node:
                return 
            currpath.append(node.val) # add node val as we descend into tree
            
            dfs(node.left)
            dfs(node.right)

            if node.left == None and node.right == None: # only want to append path at the leaf
                paths.append(currpath.copy()) # append copy so we can get curr path at the instance in time it is at a leaf 
    
            currpath.pop() # remove one node as we ascend up the tree
            return 
        dfs(root)
        # print(paths)
        for i in range(len(paths)):
            for j in range(len(paths[i])):
                paths[i][j] = str(paths[i][j])
        for i in range(len(paths)):
            paths[i] = "".join(paths[i])
        for i in range(len(paths)):
            paths[i] = int(paths[i], 2)
        return sum(paths)
                