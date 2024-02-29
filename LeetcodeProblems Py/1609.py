# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root.val % 2 == 0: # base case
            return False
        depth = 0
        queue = deque([root])
        while queue:
            level = [node.val for node in queue]
            if len(level) == 1 and depth % 2 == 0 and level[0] % 2 == 0: # even
                return False
            elif len(level) == 1 and depth % 2 != 0 and level[0] % 2 != 0: # odd
                return False

            if depth % 2 == 0: # even level
                if level[-1] % 2 == 0:
                        return False
                for i in range(len(level) - 1):
                    if level[i] % 2 == 0:
                        return False
                    elif level[i] >= level[i + 1]: 
                        return False
            if depth % 2 != 0: # odd level
                if level[-1] % 2 != 0:
                    return False
                for i in range(len(level) - 1):
                    if level[i] % 2 != 0:
                        return False
                    elif level[i] <= level[i + 1]:
                        return False
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            depth += 1
            
        return True