# 78% in time and 30% in space

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        F = Counter(nums)
        Fset = list(set(nums))
        Fsort = sorted(Fset, key=lambda x: F[x], reverse=True)
        ans = []
        for i in range(k):
            ans.append(Fsort[i])
        return ans
