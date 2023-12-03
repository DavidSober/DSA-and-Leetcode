# Ex1 num of provinces official solution 
from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in graph[node]:
                # the next 2 lines are needed to prevent cycles
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        # build the graph
        n = len(isConnected)   # n i the number of nodes (this works since the input is a matix input format)
        graph = defaultdict(list) # we will add list of neighbors for each node
        for i in range(n):
            for j in range(i + 1, n): # (REF 1) we start at i + 1 bc anything prior to that is a duplicate edge 
                                      # connection see markdown below for more information regarding this
                if isConnected[i][j]:  # in Python, 0 is considered as False, and any non-zero integer is considered as True in a Boolean context
                    graph[i].append(j) # thus if there is a non zero value in isConnected matrix we return true and do a 
                    graph[j].append(i) # bi directional connection
        
        seen = set()
        ans = 0
        
        for i in range(n):
            if i not in seen:
                # add all nodes of a connected component to the set
                ans += 1
                seen.add(i)
                dfs(i)
        
        return ans