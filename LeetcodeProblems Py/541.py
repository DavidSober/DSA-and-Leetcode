# beats 38% in time and 48% in space

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lst = list(s)
        for i in range(0, len(s), 2*k):
            lst[i:i+k] = reversed(lst[i:i+k])
        return "".join(lst)