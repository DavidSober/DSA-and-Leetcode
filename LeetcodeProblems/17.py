# beats 90% in time and 87% in space

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ""
        dic = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', 
                '7':'pqrs', '8':'tuv', '9':'wxyz'}

        ans = []
        def backtrack(curr, i):
            if len(curr) == len(digits):
                ans.append("".join(curr[:]))
                return 

            possible_letters = dic[digits[i]]
            for letter in possible_letters:
                curr.append(letter)
                backtrack(curr, i + 1)
                curr.pop()

        backtrack([], 0)
        return ans