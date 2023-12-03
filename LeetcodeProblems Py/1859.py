# beats 53% in time and 11% in space
class Solution:
    def sortSentence(self, s: str) -> str:

        lst = s.split(' ')
        order = sorted(lst, key = lambda x: x[-1])
        ret = ""
        for word in order:
            ret += word[0:-1] + " "
        return ret[0:-1]