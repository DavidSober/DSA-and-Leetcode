# beats 51% in time and 16% in space

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        F1 = Counter(word1)
        F2 = Counter(word2)
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        F1val = sorted([x for x in F1.values()])
        F2val = sorted([x for x in F2.values()])
        return F1val == F2val