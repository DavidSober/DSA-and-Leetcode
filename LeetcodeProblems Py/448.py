# beats 90% in time and 40% in space

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_set = set(nums)
        missing = []
        for i in range(1, n + 1):
            if i not in nums_set:
                missing.append(i)
        return missing  