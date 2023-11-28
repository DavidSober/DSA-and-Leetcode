class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        lst = [c for c in s] # list of the string
        for pair in shift:
            newlst = [0] * len(lst)
            if pair[0] == 0:
                # left shift direction
                for i in range(len(lst)):
                    newlst[i] = lst[(i + pair[1]) % len(lst)]
            else:
                # right shift direction
                for i in range(len(lst)):
                    newlst[i] = lst[(i - pair[1]) % len(lst)]
            lst = newlst.copy()
        return "".join(lst)