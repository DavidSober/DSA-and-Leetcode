# beats 93% in time and 40% in space

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx = max(nums)
        if len(nums) < mx + 1:
            return False
        F = Counter(nums)
        for key in F:
            if key == mx and F[key] == 2:
                continue
            elif F[key] == 1 and key != mx:
                continue
            else:
                return False
        return True 