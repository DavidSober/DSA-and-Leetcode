# faster method avoids using a set just a simple delta comparison
#beats 47% in time and 51% in space

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        delta = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] != delta:
                return False
        return True

# beats 23% in time and 20% in space

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        delta = set()
        for i in range(len(arr) - 1):
            delta.add(arr[i + 1] - arr[i])
        return len(delta) == 1