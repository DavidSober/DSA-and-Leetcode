# beats 75% in time and 57% in space

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = 0
        maxI = 0
        for i in range(len(mat)):
            ones = mat[i].count(1)

            if ones == ans:
                continue
            elif ones > ans:

                ans = max(ans, ones)
                maxI = i
        return [maxI, ans]