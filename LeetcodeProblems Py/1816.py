# took 30 seconds to get one liner
# beats 15% in time and 40% in space

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])