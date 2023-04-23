class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        pot = [i for i in range(len(nums) + 1)]
        pot_set = set(pot)
        nums_set = set(nums)
        diff = pot_set ^ nums_set
        return list(diff)[0]
        