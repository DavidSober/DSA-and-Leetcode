# beats 46% in time and 11% in space

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        for i, v in zip(s, t):
            if i in mp or v in mp.values():
                continue
            mp[i] = v
        new = ""
        for c in s:
            if c in mp:
                new += amp[c]
        return new == t