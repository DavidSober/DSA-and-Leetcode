class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        ans = 0
        j = 0
        g = sorted(g)
        s = sorted(s)
        for i in range(len(g)):
            while not (s[j] >= g[i]) and j < len(s) - 1:
                j += 1
            if s[j] >= g[i]:
                ans += 1
            if j == len(s) - 1:
                break
            j += 1
        return ans