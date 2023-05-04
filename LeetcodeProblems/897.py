# beats 7% in time and 8% in space
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        sortednodes = []
        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            sortednodes.append(node.val)
            dfs(node.right)

        dfs(root)

        def sortedArrayToBST(A): # building the new Tree with recursion make a note of this
            if not A:
                return None
            root = TreeNode(A[0])
            root.right = sortedArrayToBST(A[1:])
            return root
        ROOT = sortedArrayToBST(sortednodes)
        return ROOT

