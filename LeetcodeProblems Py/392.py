# beats 92% in time and 63% in space

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s) == 1:
            return s[0] in t
        test = deque([c for c in s])
        stack = []
        for c in t:
            if test and c == test[0]:
                stack.append(test.popleft())
        return "".join(stack) == s