# beats 98% in time and 56% in space

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = 0
        for i in range(len(arr) - 1):
            if not arr[i] < arr[i + 1]:
                break
            peak += 1
        print(peak)
        if peak == 0 or peak == len(arr) - 1:
            return False
        for i in range(peak, len(arr) - 1):
            if not arr[i] > arr[i + 1]:
                return False
        return True 