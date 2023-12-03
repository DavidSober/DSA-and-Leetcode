# beats 5% in time and 12% in space

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def isIdenticle(node1, node2):
            if node1 == None or node2 == None:
                return node1 == None and node2 == None # we make an and statement since both tree are the same
                                            #  if and only if both are null otherwise return false
            
            return (node1.val == node2.val) and isIdenticle(node1.left, node2.left) and isIdenticle(node1.right, node2.right)
        return isIdenticle(p, q)