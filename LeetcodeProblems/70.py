# this is the stairs problem and it can be solved with fib number
# seems like a probability problem but its just a fib problem
# beats 41% in time and 66% in space

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        cache = {}
        def FIB(num):
            if num == 1 or num == 2:
                return 1
            if num in cache:
                return cache[num]
            else:
                result = FIB(num - 1) + FIB(num - 2)
            cache[num] = result
            return result
        return FIB(n + 1)