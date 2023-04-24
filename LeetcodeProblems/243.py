# beats 84% in time and 99.45% in space! not bad!
# get an index list of every time word1 and word2 appear in wordsDict
# then nested for loop your way through and check the absolute diff between all possible
# indexes and keep track of the smallest. that is the ans

from collections import defaultdict

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        counter = defaultdict(list)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                counter[word1].append(i)
            elif wordsDict[i] == word2:
                counter[word2].append(i)
        
        small = float('inf')
        for i in range(len(counter[word1])):
            for j in range(len(counter[word2])):
                if abs(counter[word1][i] - counter[word2][j]) < small:
                    small = abs(counter[word1][i] - counter[word2][j])
        
        return small