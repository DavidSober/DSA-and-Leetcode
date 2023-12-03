# bin search method uses a different bin search than im used to
# not sure if this appraoch is the only way
# beats 75% in time and 10% in space

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        def testmid(mid):
            h = 0
            for pile in piles:
                h += math.ceil(pile / mid)
            return h
        while left < right:
            mid = (left + right) // 2

            if testmid(mid) <= h:  
                right = mid 
            else:
                left = mid + 1
        return right