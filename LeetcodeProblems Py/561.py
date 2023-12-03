# beats 9% in time and 5% in space
# heap is optimal solution return to this once you learn heaps

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        left = 0
        right = 1
        while right < len(nums):
            ans += min(nums[left], nums[right])
            right += 2
            left += 2
        return ans