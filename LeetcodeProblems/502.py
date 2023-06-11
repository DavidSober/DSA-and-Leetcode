# beats 37% in time and 35% in space

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        projects = list(zip(capital, profits))
        heapq.heapify(projects)
        options = []
        for i in range(k):

            while projects and projects[0][0] <= w: # if min cost of next project is affordable 
                potential_proj = heapq.heappop(projects)[1]
                heapq.heappush(options, -potential_proj)
            
            if options:
                w += -heapq.heappop(options)
        return w