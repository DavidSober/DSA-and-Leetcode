# beats 13% in time and 10% in space

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        count = Counter(nums)
        unique = 0
        for key in count:
            if count[key] == 1:
                unique += key
        return unique