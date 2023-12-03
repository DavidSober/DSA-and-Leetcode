# 40% in time and 20% in space

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True # edge case is always true
        if word[0].isupper():
            if word[1].isupper():
                for c in word:
                    if c.islower():
                        return False
                return True
            else: # if second letter is lower we check the case where only the first char is upper
                for i in range(1, len(word)):
                    if word[i].isupper():
                        return False
                return True
        else:
            for c in word:
                if c.isupper():
                    return False
            return True 
