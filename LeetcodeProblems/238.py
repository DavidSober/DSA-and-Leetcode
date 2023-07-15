# prefix product in both directions
# beats 32% in time and 21% in space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use a right and left prefix product to solve the problem I was on the right track for this one
        Lp = [nums[0]]
        for i in range(1, len(nums)):
            Lp.append(Lp[-1] * nums[i])
        
        Rp = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            Rp.append(Rp[-1] * nums[i])
        Rp = Rp[::-1]
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(Rp[1])
            elif i == len(nums) - 1:
                ans.append(Lp[-2])
            else:
                ans.append(Lp[i - 1] * Rp[i + 1])
        return ans