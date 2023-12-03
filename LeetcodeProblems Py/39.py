# beats 88% in time and 58% in space

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(curr, i):
            if sum(curr) == target:
                ans.append(curr[:])
                return
            elif sum(curr) > target:
                return

            for j in range(i, len(candidates)):
                curr.append(candidates[j])
                backtrack(curr, j)
                curr.pop()
        backtrack([], 0)
        return ans