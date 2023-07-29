# tried many methods for this problem such as splitting the tree in two 
# took 1hr
# beats 94% in time and 78% in space

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # first use dfs to build a graph that maps nodes to their neighbors (assume bidirectional graph)
        # then use a bfs graph solution to find the kth level and return that
        graph = defaultdict(list)
        seen = set([target.val])
        def dfs(node, parent):
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
            if node.right:
                graph[node.val].append(node.right.val)
            if parent:
                graph[node.val].append(parent.val)
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        #print(graph)
        queue = deque([target.val])
        level = -1
        ans = []
        while queue:
            #print([i for i in queue])
            level += 1
            if level == k:
                for i in queue:
                    ans.append(i)
                break
            for _ in range(len(queue)):
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in seen:
                        queue.append(neighbor)
                    seen.add(neighbor)
        return ans