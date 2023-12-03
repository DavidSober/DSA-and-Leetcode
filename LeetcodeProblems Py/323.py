# first graph problem complete without needing hints or solution
# beats 64% in time and 8% in space

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        seen = set()
        ans = 0
        nodesN = set()
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            nodesN.add(edge[0])
            nodesN.add(edge[1])
        
        for node in range(n):
            if node not in nodesN:
                ans += 1

        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            for i in graph[node]:
                if i not in seen:
                    dfs(i)

        for node in graph.keys():
            for neighbor in graph[node]:
                if neighbor not in seen:
                    ans += 1
                    dfs(neighbor)
        return ans