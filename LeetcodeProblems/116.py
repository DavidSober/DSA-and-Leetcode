# beats 99.95% in time and 66% in space

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = deque([root])

        while queue:
            for i in range(len(queue) - 1):
                queue[i].next = queue[i + 1]
            queue[-1].next = None 

            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root