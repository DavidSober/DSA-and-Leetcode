# beats 99% in time and 40% in space

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:

        means = set()
        sort = sorted(nums)
        for i in range(len(sort)):
            if len(sort) == 2:
                means.add( (sort[0] + sort[1]) / 2 )
                break
            means.add( (sort.pop() + sort.pop(0)) / 2)
        return len(means) 