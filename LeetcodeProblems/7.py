# beats 56% in time and 28% in space

class Solution:
    def reverse(self, x: int) -> int:
        if len(str(x)) == 1:
            return x
        neg = None
        s = str(x)
        if s[0] == "-":
            neg = True
            s = s[1:] # remove preceeding neg sign

        lst = [i for i in s]
        revlst = lst[::-1]
        # get rid of trailing zeros
        rm = 0
        for i in range(len(revlst)):
            if revlst[i] == "0":
                rm += 1
            else:
                break
        revlst = revlst[rm:]

        if neg == True:
            revlst.insert(0, '-')
        
        pn = "".join(revlst)
        num = int(pn)
        mx = (1 << 31) - 1 # signed_32bit_max
        mn = - (1 << 31) # signed_32bit_min
        if num > mx or num < mn:
            return 0
        return num