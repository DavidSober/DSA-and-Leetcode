# beats 34% in time and 69% in space

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        idx = 0
        for i in range(len(s)): 
            if idx < len(spaces) and i == spaces[idx]:
                ans.append(' ')
                idx += 1
            ans.append(s[i])
        return "".join(ans)