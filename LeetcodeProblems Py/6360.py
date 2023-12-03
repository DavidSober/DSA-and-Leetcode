# this code works but hit the time limit and thus did not count as a solution
# I need to make this faster somehow 
# constraints are below
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        arr = []
        for i in range(len(nums)):

            equal = []
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    equal.append(j)
            if len(equal) == 0:
                arr.append(0)
                continue
            absdiff = []
            for j in equal:
                absdiff.append(abs(i - j))
            arr.append(sum(absdiff))
        return arr