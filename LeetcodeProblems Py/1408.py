# beats 34% in time and 96% in space

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[j] in words[i] and i != j:
                    ans.append(words[j])
        return list(set(ans))