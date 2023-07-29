# beats 91% in time and 56% in space

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            temp = word.split(separator)
            ans.append(temp)
        ret = []
        for a in ans:
            for c in a:
                if c:
                    ret.append(c)
        return ret