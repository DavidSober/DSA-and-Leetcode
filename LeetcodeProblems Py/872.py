# old solution it is no different time and space comp but longer 
# class Solution:
#     def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#         leaf_vals = []
#         def dfs(node):
#             nonlocal leaf_vals
            
#             if not node:
#                 return 

#             if node.right == None and node.left == None:
#                 leaf_vals.append(node.val)

#             dfs(node.left)
#             dfs(node.right)

#             return 
#         dfs(root1)
#         tree1leaves = leaf_vals.copy()
#         leaf_vals = [] # need to reset vals before appending leaves of second tree
#         dfs(root2)
#         tree2leaves = leaf_vals.copy()
#         #print(tree1leaves, tree2leaves)
#         if tree2leaves == tree1leaves:
#             return True
#         else:
#             return False

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node:
                if node.right == None and node.left == None:
                    yield node.val 

                yield from dfs(node.left)
                yield from dfs(node.right)

            return 
        return list(dfs(root1)) == list(dfs(root2))