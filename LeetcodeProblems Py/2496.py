# beats 14% in time and 14% in space
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for i in range(len(strs)):

            if strs[i].isdigit():
                ans = max(ans, int(strs[i]))
            else:
                ans = max(ans, len(strs[i]))
        return ans
