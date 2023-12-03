# beats 91% in time and 50% in space

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        index = 0
        for i in range(len(nums)):

            if nums[i] != 0:
                nums[index], nums[i] = nums[i], nums[index] # RHS is a tuple we unpack it to switch nums[i] and nums[index]
                index += 1