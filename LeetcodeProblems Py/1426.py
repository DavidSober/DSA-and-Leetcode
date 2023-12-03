# beats 94% in time and 77% in space

class Solution:
    def countElements(self, arr: List[int]) -> int:
        F = Counter(arr)
        ans = 0
        for key in F:
            if F[key + 1]:
                ans += F[key]
        return ans