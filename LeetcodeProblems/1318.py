# beats 83% in time and 25% in space

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        width = max(len(format(a, 'b')), len(format(b, 'b')), len(format(c, 'b')))
        abin = format(a, f'0{width}b')
        bbin = format(b, f'0{width}b')
        cbin = format(c, f'0{width}b')
        
        flips = 0
        for i in range(len(cbin)):
            if cbin[i] == '0':
                flips += int(abin[i]) + int(bbin[i])
            else:
                if int(abin[i]) == 0 and int(bbin[i]) == 0:
                    flips += 1
        return flips