# beats 90% in time and 95% in space!

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = float('-inf')
        arr.reverse()
        for i in range(len(arr)):
            temp = arr[i]
            arr[i] = mx
            if temp > mx:
                mx = temp
        arr[0] = -1
        arr.reverse()
        return arr