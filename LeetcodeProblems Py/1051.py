# beats 85% in time 42% in space

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        expected = heights.copy()
        expected.sort()
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ans += 1
        return ans