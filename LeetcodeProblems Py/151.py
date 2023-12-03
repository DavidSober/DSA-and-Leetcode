# using built in py methods makes the problem trivial and much easier than 
# most easys that i have seen. 
# beats 95% in time and 61% in space

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])