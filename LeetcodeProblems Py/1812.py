# beats 24% in time and 8% in space
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        hset = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        coords = [hset[coordinates[0]], int(coordinates[1])]
        
        if coords[1] % 2 == 0:       # row num is even
            if coords[0] % 2 == 0: 
                return False
            else:
                return True
        else:                        # row num is odd
            if coords[0] % 2 == 0: # col num is even 
                return True
            else:
                return False