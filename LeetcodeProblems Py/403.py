# beats 48% in time and 83% in space

class Solution:
    def longestPalindrome(self, s: str) -> int:
        F = Counter(s)
        evens = 0
        odds = 0
        odddet = False
        for key in F:
            if F[key] % 2 == 0:
                evens += F[key]
            else:
                odddet = True
                odds += F[key] - 1
        if odddet:
            odds += 1
        return evens + odds