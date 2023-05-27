# beats 32% in time and 31% in space

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = set("qwertyuiop")
        r2 = set("asdfghjkl")
        r3 = set("zxcvbnm")
        ans = []
        for word in words:
            wd = set(word.lower())
            diff = r1 ^ wd
            if len(diff) == len(r1) - len(wd):
                ans.append(word)
                
            diff = r2 ^ wd
            if len(diff) == len(r2) - len(wd):
                ans.append(word)

            diff = r3 ^ wd
            if len(diff) == len(r3) - len(wd):
                ans.append(word)
        return ans