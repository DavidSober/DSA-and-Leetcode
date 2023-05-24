# beats 46% in time and 21% in space

class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)
        s = s[2:]
        s = s.zfill(32) 
        lst = [i for i in s]
        revlst = lst[::-1]
        ps = "".join(revlst)
        return int(ps, 2)