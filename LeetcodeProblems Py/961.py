# beats 99% in time and 54% in space

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        counter = defaultdict(int)
        for i in range(len(nums)):
            counter[nums[i]] += 1
            if counter[nums[i]] == 2:
                return nums[i]