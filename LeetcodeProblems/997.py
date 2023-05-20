# beats 30% in time and 36% in space

from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        vote = defaultdict(int)
        for lst in trust:
            vote[lst[1]] += 1
        pot = None
        for key in vote:
            if vote[key] == n - 1:
                pot = key
        if pot == None:
            return -1
        for lst in trust:
            if pot == lst[0]:
                return -1
        return pot