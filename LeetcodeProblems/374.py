# custom binary search that uses the api from problem statement
# 75% in time and 56% in space

class Solution:
    def guessNumber(self, n: int) -> int:

        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            feedback = guess(mid)
            if feedback == 0:
                return mid
            if feedback == 1:
                left = mid + 1
            else:
                right = mid - 1