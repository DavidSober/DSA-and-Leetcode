# two pointers on sorted list approach
# beats 54% in time and 26% in space

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = -1
        while left < right:
            if nums[left] + nums[right] < k:
                ans = max(ans, nums[left] + nums[right])
                left += 1
            else:
                right -= 1
        return ans

# binary search approach
# beats 23% in time and 64% in space

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        '''
         if k - nums[i] does not exist in the list, j will represent the index of the largest element 
         smaller than k - nums[i], which can   still contribute to finding a valid pair with a sum less than k
         '''
        nums.sort()
        ans = -1
        for i in range(len(nums)):
            j = bisect.bisect_left(nums, k - nums[i], i + 1) - 1 # ?
            if j > i:
                ans = max(ans, nums[i] + nums[j])
        return ans