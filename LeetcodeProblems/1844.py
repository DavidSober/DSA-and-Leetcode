class Solution:
    def replaceDigits(self, s: str) -> str:
        lst = [c for c in s]

        al = 'abcdefghijklmnopqrstuvwxyz'
        def shift(c, x):
            return al[al.index(c) + int(x)]

        for i in range(1, len(s)):
            if i % 2 == 0:
                continue
            else:  
                lst[i] = shift(lst[i - 1], lst[i])
        return ''.join(lst)
