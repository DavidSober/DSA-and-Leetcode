# beats 24% in time and 64% in space
# can we do better?

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        mx = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                mx = max(mx, count)
            else:
                count = 0
        return mx