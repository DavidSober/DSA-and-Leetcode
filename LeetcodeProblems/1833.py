# beats 7.5% in time and 99.7% in space

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        ans = 0
        while coins:
            if costs:
                coins -= heapq.heappop(costs)
                if coins >= 0:
                    ans += 1
            else:
                break
        return ans