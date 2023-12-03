# beats 97% in time and 57% in space

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        additions = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                i += 2
                additions += 1
                continue
            i += 1
        for i in range(additions):
            arr.pop()