# beats 20% in time and 22% in space

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        return bin(int(a, 2) + int(b, 2))[2:]