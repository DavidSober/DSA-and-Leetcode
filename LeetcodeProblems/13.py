# beats 46% in time and 10% in space 
# we had a map for adding and a map for sub (there are only 6 possible subs as per the question)
# we iterate through the string in an adjacent manner, if we find two adjacent chars in sub we append their val
# from sub and increase i by 2 to avoid double adding. 
# we also append the index of each addition so as to avoid double adding vals (we do this for both add and sub)
# if we are not subtracting then we are adding and the last 2 if statments are adding adjacent elements
# finally we check to see if we have missed adding the final number in string s, we check if that index is in
# the index list, if it is not we are missing the last number and thus we append its value and return sum for ans
class Solution:
    def romanToInt(self, s: str) -> int:
        add = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        sub = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        i = 0
        ans = []
        index = []
        while i < len(s) - 1:
            adj = s[i] + s[i + 1]
            if  adj in sub:
                ans.append(sub[adj])
                index.append(i)
                index.append(i + 1)
                i += 2
                continue 
            if i not in index:
                ans.append(add[s[i]])
                index.append(i)
            elif i + 1 not in index:
                ans.append(add[s[i + 1]])
                index.append(i + 1)
            i += 1

        if len(s) - 1 not in index:
            ans.append(add[s[-1]])
        #print(ans)
        return sum(ans)