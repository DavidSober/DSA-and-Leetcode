# beats 63% in time and 54% in space

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        ans = []
        i = j = 0
        while i < n or j < m: # note that when any index is greater than its respective string len it has no effect 
            if i < n:         # this means that when one string is finished alternating, the other string is added to the result 
                ans.append(word1[i])
            if j < m:
                ans.append(word2[j])
            i += 1
            j += 1
        return "".join(ans) 
            