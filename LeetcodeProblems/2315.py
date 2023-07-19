# beats 90% in time and 32% in space

class Solution:
    def countAsterisks(self, s: str) -> int:
        pairC = 0
        ans = 0
        for c in s:
            if pairC % 2 == 0 and c == '*':
                ans += 1
            elif c == '|':
                pairC += 1
        return ans
                