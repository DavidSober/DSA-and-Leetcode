# beats 36% in time and 8% in space
# better than before by using sumleft and sumright vars
# could use a prefix sum as well but not as efficient 
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumL = 0
        sumR = sum(nums)
        for i in range(len(nums)):
            sumR -= nums[i]
            if sumL == sumR:
                return i
            sumL += nums[i]
        return -1

# this could be a lot better let us find a faster method
# beats 5% in time and 8% in space 
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            leftsum = sum(nums[:i])
            rightsum = sum(nums[i+1:])
            if leftsum == rightsum:
                return i
        return -1