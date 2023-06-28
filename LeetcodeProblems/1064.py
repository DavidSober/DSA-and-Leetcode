# beats 82% in time and 88% in space

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if i == arr[i]:
                return i
        return -1