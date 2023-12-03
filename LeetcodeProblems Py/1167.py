# beats 51% in time and 13% in space

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            mx1 = heapq.heappop(sticks)
            mx2 = heapq.heappop(sticks)
            app = mx1 + mx2
            cost += app
            heapq.heappush(sticks, app)
        return cost