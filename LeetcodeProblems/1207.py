# beats 14% in time and 32% in space

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        F = Counter(arr)
        if len(set(F.values())) == len(F.keys()):
            return True
        else:
            return False