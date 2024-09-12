class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        diff = start ^ goal
        diff = bin(diff)[2:]
        ans = 0
        for num in diff:
            if num == '1':
                ans += 1
        return ans