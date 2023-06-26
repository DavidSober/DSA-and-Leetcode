class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """        
        i = len(s) - 1
        def rev(i):
            if i == len(s)//2 - 1:
                return
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
            i -= 1
            rev(i)
        rev(i)