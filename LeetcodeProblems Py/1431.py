class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        ans = []
        for cand in candies:
            if cand + extraCandies >= mx:
                ans.append(True)
            else:
                ans.append(False)
        return ans
            