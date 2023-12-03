# beats 92% in time and 18% in space

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [c for c in s if c.isalnum()]
        forward = "".join(lst)
        forward = forward.lower()
        backward = forward[::-1]
        return forward == backward