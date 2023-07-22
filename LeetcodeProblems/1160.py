# beats 12% in time and 35% in space

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            F = Counter(chars)
            T = Counter(word)
            state = True
            for c in T:
                if F[c] >= T[c]:
                    continue
                else:
                    state = False
            if state:
                ans += len(word)
        return ans