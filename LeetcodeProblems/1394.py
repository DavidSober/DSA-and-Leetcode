# this is much more concise but has the same time and space comp as below. however 
# it will still run much faster in practice.
# 56% in time and 15% in space
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        F = Counter(arr)
        ans = -1
        for key in F:
            if F[key] == key:
                ans = max(ans, key)
        return ans

# we can make this more concise i believe 
# beats 31% in time and 15% in space

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        F = Counter(arr)
        pot = []
        for key in F:
            if F[key] == key:
                pot.append(key)
        ret = [-x for x in pot]
        heapq.heapify(ret)
        if ret:
            return -heapq.heappop(ret) 
        else:
            return -1
