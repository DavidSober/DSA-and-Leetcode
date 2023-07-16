# beats 42% in time and 72% in space

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        comp = strs[0]
        for word in strs:
            match = 0
            for c, k in zip(word, comp):
                if c == k:
                    match += 1
                else:
                    ans.append(match)
                    break
            ans.append(match)
        return strs[0][:min(ans)]