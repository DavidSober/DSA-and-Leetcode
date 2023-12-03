# beats 65% in time and 6% in space
from sortedcontainers import SortedList
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sl = SortedList()
        queue = deque([root])
        lvl = 1
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
        ret = sl.copy()
        ret = sorted(ret, key=lambda x: (-x[0], x[1])) # sort in dec order for sum in lvl, then asceding for lvl num
        return ret[0][1]