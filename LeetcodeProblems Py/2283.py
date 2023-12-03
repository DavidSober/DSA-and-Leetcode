# beats 70% in time and 92% in space

from collections import Counter
class Solution:
    def digitCount(self, num: str) -> bool:
        A = []
        for i in range(len(num)):
            A.append(int(num[i]))

        test = Counter(A)
        for i in range(len(A)):
            if A[i] != test[i]:
                return False
        return True 