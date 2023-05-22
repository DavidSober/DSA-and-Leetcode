# beats 10% in time and 5% in space
class Solution:
    def frequencySort(self, s: str) -> str:
        F = Counter(s)
        Fsort = sorted(s, key = lambda x: (F[x], x), reverse=True)
        return "".join(Fsort)