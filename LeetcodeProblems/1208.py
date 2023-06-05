# beats 24% in time and 18% in space

from collections import deque
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        sub = deque()
        ans = i = tot = cost = currL = 0
        for j, v in enumerate(zip(s, t)):
            
            cost = abs(ord(v[1]) - ord(v[0]))
            tot += cost
            sub.append(cost)
            
            while i <= j and tot > maxCost:
                remove = sub.popleft()
                tot -= remove
                currL -= 1
                i += 1
            if tot <= maxCost:
                currL += 1
            ans = max(ans, currL)
     
        return ans