# better one liner, usese items() method, I forgot that was an option
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return[key for key, value in Counter(s1.split(' ') + s2.split(' ')).items() if value == 1]


# funny one liner

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return[key for key in Counter(s1.split(" ") + s2.split(" ")) if Counter(s1.split(" ") + s2.split(" "))[key] == 1]


# first min ans

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1 + " " + s2
        s = Counter(s.split(" "))
        ans = []
        for key in s:
            if s[key] == 1:
                ans.append(key)
        return ans