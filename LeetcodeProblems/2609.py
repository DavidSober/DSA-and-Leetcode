# beats 93% in time and 92% in space

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = 0
        for i in range(left, right + 1):
            if len(words[i]) == 1 and words[i][0] in vowels:
                count += 1
                continue
            if words[i][0] in vowels and words[i][len(words[i]) - 1] in vowels:
                count += 1

        return count