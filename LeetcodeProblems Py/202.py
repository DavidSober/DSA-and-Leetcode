class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        num = sum([int(c)**2 for c in str(n)])
        while num != 1:
            if count > 1000:
                return False
            count += 1
            num = sum([int(c)**2 for c in str(num)])
        return True