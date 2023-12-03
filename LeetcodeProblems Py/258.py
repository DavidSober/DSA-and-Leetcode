# beats 6.6% in time (oof) and 39% int space

class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            num_str = str(num)
            summ = 0
            for i in num_str:
                summ += int(i)
            print(summ, type(summ))
            if len(str(summ)) == 1:
                return int(summ)
            num = int(summ)
            