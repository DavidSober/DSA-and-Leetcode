# beats 13% in time and 7% in space

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            delta = abs(num - x)
            heapq.heappush(heap, (delta, num))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        ans.sort()
        return ans