# beats 85% in time and 51% in space

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        n = len(potions)
        potions.sort()
        for spell in spells:
            x = math.ceil(success / spell)
            pot = bisect.bisect_left(potions, x)
            print(pot)
            if pot >= n:
                ans.append(0)
                continue
            if potions[pot]*spell >= success:
                ans.append(n - pot)
        return ans