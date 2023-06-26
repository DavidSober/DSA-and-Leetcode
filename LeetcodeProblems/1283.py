# beats 12% in time and 31% in space

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(divisor):
            tot = 0
            for i in range(len(nums)):
                tot += math.ceil(nums[i] / divisor)
            return tot
        left = 1
        right = 10**6
        while left <= right:
            mid = (left + right) // 2
            if check(mid) > threshold:
                left = mid + 1
            else:
                right = mid - 1
        return left


