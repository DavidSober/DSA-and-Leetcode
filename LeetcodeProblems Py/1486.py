# beats 77% in time and 71% in space 

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            temp = start + 2 * i
            ans ^= temp
        return ans