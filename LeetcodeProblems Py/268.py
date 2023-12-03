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
        