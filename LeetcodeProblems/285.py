# beats 5.8% in time and 5.8% in space lets do better

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        suc = p.val
        temp = float('inf')
        def dfs(node):
            nonlocal suc
            nonlocal temp
            if not node:
                return 

            if node.val > p.val:
                if node.val < temp:
                    temp = node.val
                    suc = node
                

            left = dfs(node.left)
            right = dfs(node.right)
            return 
        dfs(root)
        if suc == p.val: 
            return None
        else: 
            return suc

