# beats 20% in time and 57% in space

class Solution:
    def minOperations(self, s: str) -> int:
        pot1 = "1"
        for i in range(len(s) - 1): # starts with 1
            if pot1[-1] == '1':
                pot1 += '0'
            else:
                pot1 += '1'
        pot2 = "0"
        for i in range(len(s) - 1): # starts with 0
            if pot2[-1] == '1':
                pot2 += '0'
            else:
                pot2 += '1'
        d1 = d2 = 0
        for x, y in zip(pot1, s):
            if x != y:
                d1 += 1
        for x, y in zip(pot2, s):
            if x != y:
                d2 += 1
        return min(d1, d2)
        