# the question is horribly written the dislike ratio speaks for itself
# beats 84% in time and 47% in space 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)