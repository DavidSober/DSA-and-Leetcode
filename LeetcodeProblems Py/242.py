# 11% in time and 41% in space
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = Counter(s)
        for c in t:
            if c in chars:
                chars[c] -= 1
            if c not in chars:
                return False
        for key in chars:
            if chars[key] > 0:
                return False
        return True