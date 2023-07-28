# beats 97% in time and 10% in space

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = {}
        seen = set([0])
        for i in range(len(rooms)):
            graph[i] = rooms[i]
        
        def dfs(node):
            if node in seen:
                return 
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor)

        for neighbor in graph[0]:
            if neighbor not in seen:
                dfs(neighbor)
        return len(seen) == len(rooms)