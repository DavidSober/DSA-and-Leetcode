# beats 58% in time and 97% in space

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def subsets(curr, i):
            if i > len(nums):
                return
            
            ans.append(curr[:])
            for j in range(i, len(nums)):
                curr.append(nums[j])
                subsets(curr, j + 1)
                curr.pop()
        subsets([], 0)
        return ans
    
