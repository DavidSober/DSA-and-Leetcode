# first backtrack problem getting permutations
# beats 15% in time and 73% in space

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return 
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
        backtrack([])
        return ans