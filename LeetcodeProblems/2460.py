class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        beforelen = len(nums)
        if len(nums) < 3 and nums[0] == 0:
            return [nums[1]] + [0]
        elif len(nums) < 3:
            return nums

        non_zero = []
        zero_count = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0 # del 
        for i in range(len(nums)):
            if nums[i] != 0:
                non_zero.append(nums[i])
            else:
              zero_count.append(0)
        return non_zero + zero_count

        
