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