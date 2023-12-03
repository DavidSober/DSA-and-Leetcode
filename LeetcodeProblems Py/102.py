# beats 5% in time and 9% in space

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        vals = []
        while queue:
            current_length = len(queue)
            # do logic for current level
            temp = []
            for i in range(len(queue)):
                temp.append(queue[i].val)
            vals.append(temp)
            for _ in range(current_length):
                node = queue.popleft()
                # do logic
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return vals