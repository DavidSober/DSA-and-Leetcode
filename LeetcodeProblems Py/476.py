# funny one liner version of sol
class Solution:
    def findComplement(self, num: int) -> int:
        return int("".join(["1" if c == '0' else '0' for c in bin(num)[2:]]), 2)


# forgot how to do this with a bitmask so used string stuff

class Solution:
    def findComplement(self, num: int) -> int:
        lst = [c for c in bin(num)[2:]]
        for i in range(len(lst)):
            if lst[i] == '0':
                lst[i] = '1'
            elif lst[i] == '1':
                lst[i] = '0'
        return int("".join(lst), 2)