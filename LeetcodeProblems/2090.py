# beats 30% in time and 36% in space

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = []
        # make prefix sum to avoid summing a slice which makes it TLE bc O(n^2) 
        # we make it O(N) with prefix sum
        pre = [nums[0]]
        for i in range(1, len(nums)):
            pre.append(pre[-1] + nums[i])

        for i in range(len(nums)):
            if i < k or i > len(nums) - k - 1:
                ans.append(-1)
                continue
            ans.append( (pre[i + k] - pre[i - k] + nums[i - k]) // (2*k + 1) )
        return ans