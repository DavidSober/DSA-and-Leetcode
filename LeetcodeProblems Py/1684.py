class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_s = set(allowed)
        ans = 0
        for word in words:
            good = True
            for c in word:
                if c not in allowed_s:
                    good = False 
                    break
            if good:
                ans += 1
        return ans