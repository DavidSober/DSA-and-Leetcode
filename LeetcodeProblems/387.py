# beats 78% in time and 21% in space

class Solution:
    def firstUniqChar(self, s: str) -> int:
        F = Counter(s)
        pot = []
        for key in F:
            if F[key] == 1:
                pot.append(key)
        if not pot:
            return -1
        for i in range(len(s)):
            if s[i] in pot:
                return i