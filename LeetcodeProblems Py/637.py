# beats 96% in time and 36% in space


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = deque([root])

        while queue:
            current_length = len(queue)
            
            vals = [i.val for i in queue] # holds vals for curr level
            ans.append(sum(vals) / len(queue)) # we append the mean value for each level

            for _ in range(current_length):
                node = queue.popleft()
                # do logic
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans 
