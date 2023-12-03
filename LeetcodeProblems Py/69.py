# beats 57% in time and 14% in space

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 2
        right = x//2 # i had this at L = 0 and R = x but this is a faster range
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right