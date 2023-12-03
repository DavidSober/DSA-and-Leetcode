# beats 64% in time and 6% in space

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # main idea here is we need to find the first index where the sorting fails and then we find the last index
        # when sorting fails. the delta between those two indexes will be the answer
        # so instead of using a mono stack (like I did the first time) lets use a sorted copy of nums to compare nums to
        # let us also have an index i so that we can keep track of which indexs in nums do not match nums_sorted 
        nums_sorted = sorted(nums)
        mismatch = []
        i = 0
        for x, y in zip(nums, nums_sorted):

            if x != y:
                mismatch.append(i)
            i += 1

        if mismatch:
            return mismatch[-1] - mismatch[0] + 1 # calculates delta between indexes aka the span of the subarr
        else:
            return 0


