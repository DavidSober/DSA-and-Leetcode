# beats 86% in time and 22% in space

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        F = Counter(nums)
        return F[target] > len(nums) / 2