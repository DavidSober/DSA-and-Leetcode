# beats 15% in time and 52% in space
# slow bc O(N^2)

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        ans = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] - nums[j] == k and i != j:
                    ans += 1

        return ans 