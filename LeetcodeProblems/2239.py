# first problem after 8 day vacation
# beats 22% in time and 90% in space

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            delta = abs(num)
            if not ans:
                ans.append(num)
            elif abs(ans[-1]) == abs(num):
                ans.append(num)
            elif abs(ans[-1]) > abs(num):
                ans = []
                ans.append(num)
                continue
        return max(ans)