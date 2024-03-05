class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 1:
            return 1
        lst = [c for c in s]
        while lst and lst[0] == lst[-1]:
            if len(lst) == 1:
                break
            pre = 0
            for i in range(len(lst)):
                if lst[i] == lst[0]:
                    pre += 1
                else:
                    break
            suf = len(lst)
            for i in range(len(lst) - 1, -1, -1):     
                if lst[i] == lst[0]:
                    suf -= 1
                else:
                    break
            lst = lst[pre : suf]
        return len(lst)
