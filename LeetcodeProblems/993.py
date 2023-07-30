# beats 96% in time and 34% in space

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        def dfs(node, parent):
            if not node:
                return
            
            node.parent = parent

            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        queue = deque([root])
        while queue:
            vals = [i.val for i in queue]
            x_node = None
            y_node = None
            for node in queue:
                if node.val == x:
                    x_node = node
                elif node.val == y:
                    y_node = node
            if x_node and y_node:
                if x_node.val in vals and y_node.val in vals and x_node.parent != y_node.parent:
                    return True

            for _ in range(len(queue)):

                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return False