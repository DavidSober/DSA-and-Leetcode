class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return [n**2 for n in sorted(nums, key=lambda x: x**2)]