class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        allow = set(allowed)
        counter = 0
        for word in words:
            for letter in word:
                if letter not in allow:
                    counter += 1
                    break # enures that once a single letter is wrong we skip the rest of the word
        
        return len(words) - counter # diff of total and wrong words is ans
    # it is the same principle as a complement 
