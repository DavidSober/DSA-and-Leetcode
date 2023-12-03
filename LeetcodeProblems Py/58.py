# beats 44% in time and 13% in space

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])