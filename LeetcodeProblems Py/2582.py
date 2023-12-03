# beats 27% in time and 41% in space

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        per = 1
        turn = True # T means fowards F means reverse
        while time:
            if turn:
                per += 1
            else:
                per -= 1
            if per == n:
                turn = False
            elif per == 1:
                turn = True 

            time -= 1
            
        return per