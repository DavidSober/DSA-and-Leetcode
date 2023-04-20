# beats 45% in time and 35% in space

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            temp = str(nums[i])
            if len(temp) % 2 == 0:
                count += 1
            
        return count 