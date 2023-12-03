# beats 55% in time and 20% in space

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        seen = set([source])

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node):
            if node in seen:
                return 
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor)

        for neighbor in graph[source]:
            if neighbor not in seen:
                dfs(neighbor)
        return destination in seen