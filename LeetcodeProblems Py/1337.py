# this solution uses a heap.. seems easier than sorted somehow...
# beats 33% in time and 17% in space

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(len(mat)):
            strength = sum(mat[i]) # num of soldiers
            heapq.heappush(heap, [strength, i])
        ret = heapq.nsmallest(k, heap)
        ans = [x[1] for x in ret]
        return ans

# beats 41% in time and 17% in space
# can we do it with a heap?

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rowS = []
        for i in range(len(mat)):
            strength = sum(mat[i]) # num of soldiers
            rowS.append([strength, i])
        ret = sorted(rowS, key=lambda x: x[0]) # sorts rows based off num of soldiers
        ans = []
        for i in range(k):
            ans.append(ret[i][1])
        return ans
        