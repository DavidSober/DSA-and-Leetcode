# medium in 15:53

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = []
        for num in nums:
            string = str(num)
            lst = [int(c) for c in string]
            for i in range(len(lst)):
                lst[i] = mapping[lst[i]] # mapping here
            # convert back into num
            lst = [str(n) for n in lst]
            lst = int("".join(lst))
            # lst is now the converted int
            mapped.append([num, lst])
        # mapped is populated
        sl = sorted(mapped, key=lambda x: (x[1]))
        return [pair[0] for pair in sl]
