# beats 5% in time and 12% in space
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        temp = []
        def dfs(node):
            if not node:
                return 
            temp.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root1)
        tree1 = temp.copy()
        temp = []
        dfs(root2)
        tree2 = temp.copy()

        for i in range(len(tree1)):
            for j in range(len(tree2)):
                if tree1[i] + tree2[j] == target:
                    return True
        return False