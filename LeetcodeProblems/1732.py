# beats 10% in time and 58% in space

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = 0
        maxh = 0
        for i in gain:
            h += i
            maxh = max(maxh, h)
        return maxh