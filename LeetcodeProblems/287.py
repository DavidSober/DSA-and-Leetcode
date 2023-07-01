# beats 24% in time 64% in space

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            delta = nums[i + 1] - nums[i]
            if delta == 0:
                return nums[i]