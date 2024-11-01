class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 2:
            return s
        last2 = []
        ans = ""
        for c in s:
            if len(last2) < 2:
                last2.append(c)
            else:
                if last2[0] == last2[1] == c:
                    continue
                else:
                    ans += last2[0]
                    last2[0] = last2[1]
                    last2[1] = c
        return ans + last2[0] + last2[1]