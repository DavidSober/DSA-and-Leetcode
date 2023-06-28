# bin search solution is much better logn << n 
# beats 92% in time and 46% in space
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= mid:
                right = mid - 1
            else:
                left = mid + 1
        if left > len(arr) - 1 or arr[left] != left:
            return -1
        return left 

# beats 82% in time and 88% in space

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if i == arr[i]:
                return i
        return -1