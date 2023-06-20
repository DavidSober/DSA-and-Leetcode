# used binary search for this one
# beats 21% in time and 87% in space

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        L = bisect.bisect_left(nums, target)
        R = bisect.bisect_right(nums, target)
        return R-L > len(nums) / 2

# beats 86% in time and 22% in space

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        F = Counter(nums)
        return F[target] > len(nums) / 2