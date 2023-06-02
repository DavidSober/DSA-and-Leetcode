# i had to add 3 if statements just for edge cases... find a way to avoid that
# beats 45% in time and 54% in space

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if s == pattern and len(s) == len(pattern) == 1:
            return True
        elif s == pattern:
            return False
        mp = {}
        s = s.split()
        if len(s) == 1 and len(pattern) != 1:
            return False
        for i in range(len(pattern)):
            if pattern[i] in mp or s[i] in mp.values():
                continue
            mp[pattern[i]] = s[i]
        test = []
        for c in pattern:
            if c in mp:
                test.append(mp[c])
        return test == s