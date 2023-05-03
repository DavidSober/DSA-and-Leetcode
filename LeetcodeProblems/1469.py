# beats 20% in time and 6.7% in space
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        loner = []
        def dfs(node):
            if not node:
                return

            if node.right and not node.left:
                loner.append(node.right.val)
            elif not node.right and node.left:
                loner.append(node.left.val)


            dfs(node.left)
            dfs(node.right)

            return 
        dfs(root)
        return loner