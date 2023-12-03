# beats 23% in time and 37% in space
# uses heap (problem says use floor but you need to use ceiling instead..)
import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-num for num in piles] # negate
        heapq.heapify(piles) 
        for i in range(k):
            num = -heapq.heappop(piles) # negat again before operations
            num = -math.ceil(num/2)
            heapq.heappush(piles, num) # note if we do not pop and push the heap property might not remain
        return -sum(piles)
