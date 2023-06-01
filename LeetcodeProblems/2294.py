# beats 13% in time and 5% in space

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        mn = mx = 0
        sub = []
        temp = []
        ans = 0
        while mx < len(nums):
            minval = nums[mn]
            maxval = nums[mx]
            delta = abs(minval - maxval)
            if not delta <= k:
                temp = nums[mn:mx]
                sub.append(temp)
                mn = mx
                continue
            mx += 1
        ans += len(sub)
        ans += 1 # we always miss the last subsequence bc we detect the subsequence in post
        return ans 