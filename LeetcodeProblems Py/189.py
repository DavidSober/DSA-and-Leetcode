# beats 31% in time and 11% in space

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = []
        n = len(nums)
        for i in range(n):
            idx.append( ( (i + k) % n, nums[i]) )
        idx.sort()
        for i in range(len(idx)):
            nums[i] = idx[i][1]