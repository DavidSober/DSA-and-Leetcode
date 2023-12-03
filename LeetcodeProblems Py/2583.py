# beats 26% in time and 22% in space
from sortedcontainers import SortedList
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sl = SortedList()
        queue = deque([root])
        lvl = 0
        while queue:
            current_length = len(queue)
            # do logic for current level
            tot = 0
            for node in queue:
                tot += node.val
            sl.add((tot, lvl))
            lvl += 1
            for _ in range(current_length):
                node = queue.popleft()
                # do logic
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        if lvl < k:
            return -1 # if k was never reached
        else:
            return sl[-k][0] # kth largest sum, lvl for that sum