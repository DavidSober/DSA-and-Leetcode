# I did not write this but it has the comments needed to understand what i 
#  wrote after. it is the same idea basically. 
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # Check for all subtree rooted at all nodes of tree "root"
        def dfs(node):

            # If this node is Empty, then no tree is rooted at this Node
            # Thus "tree rooted at node" cannot be same as "rooted at subRoot"
            # "tree rooted at subRoot" will always be non-empty (constraints)
            if node is None:
                return False

            # If "tree rooted at node" is identical to "tree at subRoot"
            elif is_identical(node, subRoot):
                return True

            # If "tree rooted at node" was not identical.
            # Check for tree rooted at children
            return dfs(node.left) or dfs(node.right)

        def is_identical(node1, node2):

            # If any one Node is Empty, both should be Empty
            if node1 is None or node2 is None:
                return node1 is None and node2 is None

            # Both Nodes Value should be Equal
            # And their respective left and right subtree should be identical
            return (node1.val == node2.val and
                    is_identical(node1.left, node2.left) and
                    is_identical(node1.right, node2.right))

        # Check for node rooted at "root"
        return dfs(root)
'''
Above is what below is based off of 
'''
# This is the fast option to write but timp comp is way worse than serialization
# as shown below. above this is the code i based this off it comes with comments
# beats 35% in time and 11% in space
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def SameTreeChecker(node1, node2):
            if not node1 or not node2:
                return node1 == None and node2 == None

            return (node1.val == node2.val) and (SameTreeChecker(node1.left, node2.left) and (SameTreeChecker(node1.right, node2.right)))

        def dfs(node):
            if not node:
                return 
            
            if SameTreeChecker(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)  
            
        return dfs(root)





# Serialization of the tree paths
# this approach works and is good to know but there might be a more simple one
# beats 92% in time and 6% in space
'''
Note that below approach is serialization and works well is one of the 
fastest options but it is not the easiest to come up with on the fly... for most
'''

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