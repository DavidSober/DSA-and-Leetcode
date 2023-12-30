class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True
        F = Counter()
        for word in words:
            for c in word:
                F[c] += 1
        S = set(F.values()) # has unique frequencies of chars in words
        for freq in S:
            if freq / len(words) == freq // len(words): # if freq of unique chars evenly distributes into num of spaces
                continue                                # then we know for that char all strings are equal
            else:
                return False
        return True