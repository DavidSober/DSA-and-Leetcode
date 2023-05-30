# beats 15% in time and 30% in space

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        val = 0
        while len(nums) > 1:
            v1 = nums.pop(0)
            v2 = nums.pop(-1)
            con = int(str(v1) + str(v2))
            val += con
        if nums:
            val += nums[0]
        return val