# beats 5% in time and 7% in space

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret = []
        
        def dfs(node):
            if not node:
                return 
            for child in node.children:
                dfs(child)
            ret.append(node.val)
            return 
        dfs(root)
        return ret