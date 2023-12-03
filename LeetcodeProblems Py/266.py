
# 61% in time and 5% in space
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        F = Counter(s)
        l = len(s)
        if l % 2 == 0: # even
            for key in F:
                if F[key] % 2 != 0:
                    return False
            return True

        else: # odd
            ones = 0
            for key in F:
                if F[key] != 2 and ones > 1:
                    return False
                elif F[key] == 1:
                    ones += 1
            return True
