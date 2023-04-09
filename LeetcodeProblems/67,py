class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)): # convert ints in digits into strings
            digits[i] = str(digits[i])
        string = "".join(digits) # convert list of strings into one string
        num = int(string) # convert string into num
        result = num + 1 # do the math
        b2s = str(result) # convert back to string hence: b2s
        ans = []
        for i in range(len(b2s)):
            ans.append(int(b2s[i])) # convert string into int and append to ans
        return ans                  # thus making ans a list of ints as requested