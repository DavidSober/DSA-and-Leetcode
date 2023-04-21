# 99% in time and 16% space

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        hset = set(nums)

        back = sorted(list(hset), reverse=True)
        if not len(back) > 2:
            return max(nums) 
        else:
            top3 = back[0:3]
            return min(top3)