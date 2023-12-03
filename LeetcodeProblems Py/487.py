# beats 67% in time and 70% in space

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pre = -1 # needs to be -1 bc of ans calc imagine passing nums = [1] and you will get why prev is -1
        curr = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                pre = curr
                curr = 0
            else:
                curr += 1
            ans = max(ans, pre + 1 + curr) # num of consec ones is all [prev ones + one zero + ones after] 

        return ans