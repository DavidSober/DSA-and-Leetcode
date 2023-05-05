# beats 80% in time and 20% in space
# classic sliding window problem
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(('a', 'e', 'i', 'o', 'u'))
        count = 0
        ans = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        ans = count

        for i in range(k, len(s)):
            
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            ans = max(ans, count)
        
        return ans