class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            lst = [c for c in word]
            rev = lst[::-1]
            if lst != rev:
                continue
            return word
        return ""