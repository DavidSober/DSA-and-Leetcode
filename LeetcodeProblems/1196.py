# beats 86% in time and 73% in space

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        ans = 0
        cap = 5000
        weight.sort()
        for num in weight:
            cap -= num
            if cap < 0:
                break
            ans += 1
        return ans