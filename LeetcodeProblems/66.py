# beats 60% in time and 17% in space

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for d in digits:
            num += str(d)
        I = int(num)
        res = I + 1
        b2s = str(res)
        ret = []
        for i in b2s:
            ret.append(int(i))
        return ret