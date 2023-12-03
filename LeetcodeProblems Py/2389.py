# beats 9% in time and 18% in space

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        heapq.heapify(nums)
        ans = []
        for i in range(len(queries)):
            temp = nums.copy()
            tot = 0
            L = 0
            while temp:
                mn = heapq.heappop(temp)
                tot += mn
                if tot > queries[i]:
                    break
                L += 1
            ans.append(L)
        return ans