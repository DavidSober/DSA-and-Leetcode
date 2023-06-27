# very similar solution to the ways to cut a chocolate problem 
# figured it out after a could WAs right bound has to be reficulously high
# for some edge cases
# beats 75% in time and 99% in space

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = 10**9
        while left <= right:
            mid = (left + right) // 2
            subsum = splits = 0
            for num in nums:
                subsum += num
                if not subsum <= mid:
                    subsum = num
                    splits += 1
            if splits < k:
                right = mid - 1
            else:
                left = mid + 1
        return left