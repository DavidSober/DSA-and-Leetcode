# beats 59% in time and 10% in space

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        temp = [c for c in s]
        left = 0
        right = len(s) - 1
        while left < right:
            if not (temp[right].islower() or temp[right].isupper()):
                right -= 1
            elif not (temp[left].islower() or temp[left].isupper()):
                left += 1
            else:
                temp[left], temp[right] = temp[right], temp[left]
                left += 1
                right -= 1
        return "".join(temp)