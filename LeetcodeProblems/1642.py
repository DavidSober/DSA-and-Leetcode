# beats 76% in time and 46% in space

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        brickallocation = []
        for i in range(len(heights) - 1):
            
            delta = heights[i + 1] - heights[i]
            if delta <= 0:
                continue

            heapq.heappush(brickallocation, -delta)
            bricks -= delta

            if ladders == 0 and bricks < 0:
                return i

            if bricks < 0:
                bricks += -heapq.heappop(brickallocation)
                ladders -= 1

        return len(heights) - 1