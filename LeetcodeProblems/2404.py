# beats 28% in time and 5% in space

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = Counter(nums)
        newF = { key:value for key, value in freq.items() if key % 2 == 0 }
        if not newF:
            return -1
        Fsorted = dict(sorted(newF.items(), reverse=True))
        maxV = max(Fsorted.values())
        F = { k:v for k, v in Fsorted.items() if v == maxV}
        MinK = min(F)
        return MinK