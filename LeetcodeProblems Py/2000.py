# beats 6% in time and 25% in space

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        idx = word.index(ch)
        rev = word[0:idx + 1]
        rest = word[idx + 1 :]
        return rev[::-1] + rest