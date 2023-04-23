# beats 97% in time and 99% in space that was ez 

class Solution:
    def numberOfSteps(self, num: int) -> int:

        ans = 0
        while 0 < num:

            if num % 2 == 0:
                num = num / 2
                ans += 1
            else:
                num -= 1
                ans += 1
        return ans 