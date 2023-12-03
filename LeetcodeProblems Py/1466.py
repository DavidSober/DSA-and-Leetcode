# beats 99.33% in time and 8% in space

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        Ngraph = defaultdict(list)
        Ingraph = defaultdict(list)
        ans = 0
        seen = set()
        p2zero = set([0])
        for x, y in connections:
            Ngraph[x].append(y)
            Ngraph[y].append(x)
        for x, y in connections:
            Ingraph[y].append(x)

        def dfs(node):
            nonlocal ans
            if node in seen:
                return
            seen.add(node)
            for neighbor in Ngraph[node]:
                if neighbor not in seen and neighbor not in p2zero:
                    if node in Ingraph[neighbor]:
                        # print(node, neighbor)
                        ans += 1
                    p2zero.add(neighbor)
                    dfs(neighbor)

        for neighbor in Ngraph[0]:
            if neighbor not in seen:
                if 0 in Ingraph[neighbor]:
                    ans += 1
                p2zero.add(neighbor)
                dfs(neighbor)
        # print(Ngraph)
        #print(Ingraph)
        return ans