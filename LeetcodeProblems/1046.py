# here is the heap solution (my solution performed better consisently despite
# time comp considering heap to be better)
# time 29% time and 11% space
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones] # we are negating the stone, this must be done in order to access the 
                                      # largest element in stones with heap (default is min element)
        heapq.heapify(stones)
        while len(stones) > 0:
            if len(stones) == 1:
                return abs(stones[0]) # read comment below for abs
            mx1 = abs(heapq.heappop(stones)) # we need to use abs since we negated the list ealier
            mx2 = abs(heapq.heappop(stones))
            if mx1 != mx2:
                mx1 = mx1 - mx2
                heapq.heappush(stones, -mx1) # we must re negate the element before we push back in order to keep sorted
            if len(stones) == 0:
                return 0

# beats 60% in time and 93% in space

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 0 :
            if len(stones) == 1:
                return stones[0]
            max1 = stones.pop(stones.index(max(stones)))
            max2 = stones.pop(stones.index(max(stones)))
            
            if max1 != max2:
                max1 = max1 - max2
                stones.append(max1)
            if len(stones) == 0:
                return 0
