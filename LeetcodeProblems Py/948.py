class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        mx = 0
        while tokens:
            mx = max(mx, score)
            if power < tokens[0]:
                if score:
                    power += tokens.pop()
                    score -= 1
                    continue
                else:
                    break
            if power >= tokens[0]:
                power -= tokens.pop(0)
                score += 1
            mx = max(mx, score)    
        return mx
