# O(n * k) not sure that this is better
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        F = Counter(nums)
        ans = []
        for i in range(k):
            mx = max(F, key = lambda x: F[x])
            ans.append(mx)
            F[mx] = 0
        return ans 

# 46% in time and 51% in space
# time comp for this is O(N log N) can we do better? yes
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        F = Counter(nums)
        Fset = list(set(nums))
        Fsort = sorted(Fset, key=lambda x: F[x], reverse=True)
        ans = []
        for i in range(k):
            ans.append(Fsort[i])
        return ans
