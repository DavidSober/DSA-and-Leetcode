# beats 34% in time and 11% in space

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        dict = defaultdict(list)
        for i in range(len(nums)):
            dict[nums[i]].append(i)
        # i figured out a math series formula for this it is on github
        for key in dict:
            j = 1
            for i in range(len(dict[key])):
                ans += len(dict[key]) - j
                j += 1
        return ans