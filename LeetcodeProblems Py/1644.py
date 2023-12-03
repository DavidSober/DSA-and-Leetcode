# beats 25% in time and 10% in space

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path = []
        found = False
        def dfs(node, match):
            nonlocal found
            if not node:
                return
            if found == True:
                return  
            path.append(node)
            if node.val == match.val:
                found = True
                return
            dfs(node.left, match)
            dfs(node.right, match)
            if not found:
                path.pop()
        dfs(root, p)
        p1 = path.copy()
        path = []
        found = False
        dfs(root, q)
        p2 = path
        if not p1 or not p2:
            return None
        # t1 = [n.val for n in p1] # for debugging 
        # t2 = [n.val for n in p2]
        # print(t1, t2)
        p1.reverse()
        for node in p1:
            if node in p2:
                return node

