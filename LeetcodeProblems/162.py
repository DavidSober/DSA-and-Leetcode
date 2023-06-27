# bin search
# beats 72% in time and 32% in space

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return nums.index(max(nums))
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        if right == -1:
            return nums.index(max(nums))
        return right