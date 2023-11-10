class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        F = Counter()
        for pair in adjacentPairs:
            F[pair[0]] += 1
            F[pair[1]] += 1
        for key in F:
            if F[key] == 1:
                start = key
                break
        graph = defaultdict(list)
        for pair in adjacentPairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        seen = set()
        ans = []
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            ans.append(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        dfs(start)
        return ans
        