# 38% in time and 7% in space

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if(n <= 1):
            return n == 1

        return n % 3 == 0 and self.isPowerOfThree(n / 3)