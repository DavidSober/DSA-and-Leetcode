# beats 68% in time and 47% in space

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        target = [nums[0]]
        for i in range(1, len(nums)):
            
            target.insert(index[i], nums[i])

        return target
