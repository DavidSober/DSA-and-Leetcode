# beats 18% in time and 31% in space

class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.c1 = [0]*n
        self.r1 = [0]*n
        self.d1 = [0, 0]

        self.c2 = [0]*n
        self.r2 = [0]*n
        self.d2 = [0, 0]

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n

        if player == 1:
            self.c1[col] += 1
            self.r1[row] += 1
            if row == col:
                self.d1[0] += 1
            if row + col == n - 1:
                self.d1[1] += 1
        else:
            self.c2[col] += 1
            self.r2[row] += 1
            if row == col:
                self.d2[0] += 1
            if row + col == n - 1:
                self.d2[1] += 1 
                
        if n in self.c1 or n in self.r1 or n in self.d1:
            return 1
        if n in self.c2 or n in self.r2 or n in self.d2:
            return 2
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)