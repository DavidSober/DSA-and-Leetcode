# beats 99.9% in time and 40% in space

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        ans = 0
        seen = set([0])
        restricted = set(restricted)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node):
            if node in seen or node in restricted:
                return
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen and neighbor not in restricted:
                    dfs(neighbor)

        for neighbor in graph[0]:
            if neighbor not in seen and neighbor not in restricted:
                dfs(neighbor)
        return len(seen)