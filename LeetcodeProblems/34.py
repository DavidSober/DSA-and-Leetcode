# beats 83% in time and 97% in space 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, right - 1] # need to subtract 1 from right bc bisect right shows where you should insert the index which 
                                 # is one number off the index of the rightmost position of target... lol