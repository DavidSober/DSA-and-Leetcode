# beats 60% in time and 7% in space

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        cache = {}
        def Pnum(row, col):
            if row == 0 or col == 0 or row == col:
                return 1
            if (row, col) in cache:
                return cache[(row, col)]
            else:
                result = Pnum(row - 1, col - 1) + Pnum(row - 1, col)
            cache[(row, col)] = result
            return result
        ans = []
        for row in range(numRows): 
            temp = []
            for col in range(row + 1): # + 1convert to 1 index num of cols
                temp.append(Pnum(row, col))
            ans.append(temp)
        return ans
