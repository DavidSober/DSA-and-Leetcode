# converted it to one liner
# beats 80%  in time and 23% in space
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum([int(c) for c in bin(x^y)[2:]])

# we can see what bits changed using XOR
# beats 52% in time and 92% in space

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        tot = 0
        for c in bin(z)[2:]:
            tot += int(c)
        return tot