# 30% in time and 35% in space
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        F = Counter(nums)
        ans = [0,0]
        for key in F:
            if F[key] == 1:
                ans[1] += 1
                continue
            if F[key] % 2 == 0: # even
                ans[0] += F[key] / 2
            else: # odd
                ans[0] += (F[key] - 1) / 2
                ans[1] += 1
        ans[0] =  int(ans[0])
        return ans