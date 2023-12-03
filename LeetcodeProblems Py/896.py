# beats 38% in time and 57% in space

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                break
            if nums[i] <= nums[i + 1] and i == len(nums) - 2:
                return True
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                break
            if nums[i] >= nums[i + 1] and i == len(nums) - 2:
                return True
        return False