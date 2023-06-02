# beats 66% in time and 9% in space

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        move = {'N': (0, 1), 'S': (0, -1), 'E': (1,0), 'W': (-1,0)}
        past = set()
        past.add((0,0)) # we have to use .add bc if you pass a tuple into a set as an arg it will iterate and add the elements
                        # that would result in a set = {0} which is not what we want
        x,y = 0,0
        for c in path:
            x += move[c][0]
            y += move[c][1]
            if (x,y) in past:
                return True
            past.add((x,y))
        return False    
        