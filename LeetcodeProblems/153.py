# beats 85% in time and 86% in space

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] < nums[0]:
                right = mid - 1
            else:
                left = mid + 1

        if left >= len(nums):
            left = 0 
        return nums[left]
