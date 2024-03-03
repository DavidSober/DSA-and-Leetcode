# nlogn time comp and constant space comp. I revisited this by chance. 
# best sol is still the bottom one here which i did not come up with
# you could also learn the gauss sum if you want
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] == 0:
            return 1
        if len(nums) == 0 and nums[0] == 1:
            return 0
        nums.sort()
        if len(nums) - nums[-1] != 0:
            return len(nums)
        if 0 not in nums:
            return 0
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] != 1:
                return nums[i] + 1


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        pot = [i for i in range(len(nums) + 1)]
        pot_set = set(pot)
        nums_set = set(nums)
        diff = pot_set ^ nums_set
        return list(diff)[0]
    
# my first one liner! uses bitwise difference
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return list(set(nums) ^ set([i for i in range(len(nums) + 1)]))[0]
        
# another one liner but much better stats: uses sum difference 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum((i for i in range(0, len(nums) + 1))) - sum((i for i in nums))
        