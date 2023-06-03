# classic two pointer approach
# beats 62% in time and 12% in space

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # two pointers
        i = tot = ans = 0
        seen = set()
        for j in range(len(nums)):
            
            while i < j and nums[j] in seen: # if j in seen we need to remove elements from the left 
                tot -= nums[i]
                seen.remove(nums[i])
                i += 1
            tot += nums[j]
            ans = max(ans, tot)
            seen.add(nums[j])
        return ans