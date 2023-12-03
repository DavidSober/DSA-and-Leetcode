# beats 86% in time and 78% in space

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        if not nums:
            return [[lower, upper]]
        if nums[0] != lower:
            nums = [lower - 1] + nums 
        if nums[-1] != upper:
            nums.append(upper + 1)
        for i in range(len(nums)- 1):
            if nums[i + 1] == nums[i] + 1:
                continue
            else:
                ans.append([nums[i] + 1, nums[i + 1] - 1])
        return ans