# yes you can use nsmallest but it is much slower than either sorting or using a for loop with heapqheappop
# beats 20% in time and 28% in space
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        delta = []
        for point in points:
            r = ((point[0])**2 + (point[1])**2)**0.5
            heapq.heappush(delta, (r, point))
        small = heapq.nsmallest(k, delta)
        ans = [x[1] for x in small]
        return ans

# sure enough we can use a heap and it was perhaps even easier using it 
# I think we are supposed to use heapq.nlargest... we could try that why not
# beats 45% in time and 45% in space
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        delta = []
        for point in points:
            r = ((point[0])**2 + (point[1])**2)**0.5
            heapq.heappush(delta, (r, point))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(delta)[1])
        return ans


# i decided to see if i could do this without a heap and sure enough you can
# beats 52% in time and 32% in space
# lets try heap next
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        delta = []
        for point in points:
            r = ((point[0])**2 + (point[1])**2)**0.5
            delta.append((r, point))
        ret = sorted(delta, key=lambda x: x[0])
        ans = ret[:k]
        ans = [x[1] for x in ans]
        return ans