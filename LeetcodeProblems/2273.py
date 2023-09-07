# beats 5% in time and 17% in space

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        while True:
            if len(words) < 2:
                break
            flag = False
            for i in range(len(words) - 1):
                F1 = Counter(words[i])
                F2 = Counter(words[i + 1])
                if F1 == F2:
                    words.pop(i + 1)
                    flag = True
                    break
            if flag == False:
                break
        return words