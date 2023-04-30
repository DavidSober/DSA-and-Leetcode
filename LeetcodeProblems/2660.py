# from contest 343 no stats to show right now come back later

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
            
        stackA = []
        stackB = []
        Ascore = 0
        Bscore = 0
        for x, y in zip(player1, player2):

            if 10 in stackA[-2:]:
                Ascore += 2 * x
            else:
                Ascore += x

            if 10 in stackB[-2:]:
                Bscore += 2 * y
            else:
                Bscore += y
            stackA.append(x)
            stackB.append(y)

        if Ascore == Bscore: 
            return 0
        if Ascore > Bscore: 
            return 1
        else: return 2