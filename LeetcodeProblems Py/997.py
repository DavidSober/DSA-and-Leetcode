# revisit after many months 
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates = []
        F_right = Counter()
        F_left = Counter()
        for pair in trust:
            F_right[pair[1]] += 1
        for pair in trust:
            F_left[pair[0]] += 1
        for i in range(1, n + 1):
            if i not in F_left.keys():
                candidates.append(i)
        for candidate in candidates:
            if F_right[candidate] == n - 1:
                return candidate
        return -1


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