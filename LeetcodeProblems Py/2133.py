# beats 90% in time and 30% in space

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        ans = 0
        for i in range(len(sentences)):
            temp = sentences[i].split(' ')
            ans = max(ans, len(temp))
        
        return ans