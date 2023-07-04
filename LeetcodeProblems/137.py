# read comment
# beats 94% in time and 35% in space

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # this might not fit the constant space constraint
        F = Counter(nums)
        for key in F:
            if F[key] == 1:
                return key