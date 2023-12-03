# beats 60% in time and 14% in space

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        F = Counter(s)
        order = [c for c in order]
        neworder = [c for c in order if c in s]
        new = ""
        for c in neworder:
            for i in range(F[c]):
                new += c
        diff = [c for c in s if c not in new]
        while diff:
            new += diff.pop(0)
        return new
