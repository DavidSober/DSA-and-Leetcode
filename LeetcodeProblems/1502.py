# beats 23% in time and 20% in space

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        delta = set()
        for i in range(len(arr) - 1):
            delta.add(arr[i + 1] - arr[i])
        return len(delta) == 1