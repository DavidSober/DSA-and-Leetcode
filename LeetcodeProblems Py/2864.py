class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        lst = [c for c in s]
        F = Counter(lst)
        if F['1'] == 1:
            return '0' * (len(s) - 1) + '1'
        return '1' * (F['1'] - 1) + '0' * (len(s) - F['1']) + '1' 