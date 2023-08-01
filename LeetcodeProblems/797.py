# beats 95% in time and 15% in space

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        graphN = defaultdict(list)
        for i in range(len(graph)):
            for neighbor in graph[i]:
                graphN[i].append(neighbor)
        
        seen = set()
        def backtrack(curr, i):
            if i == len(graph) - 1:
                ans.append(curr[:])
                return
        
            for neighbor in graph[i]:
                if neighbor not in curr:
                    print(neighbor)
                    curr.append(neighbor)
                    backtrack(curr, neighbor)
                    curr.pop()
            
        backtrack([0], 0)
        return ans