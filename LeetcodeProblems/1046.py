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
