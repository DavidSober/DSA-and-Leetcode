# if you concat a string to itself and iterate through it, 
# you can go though all possible rotations of that string in linear time.
# nice trick
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = s + s
        for i in range(0, len(s) // 2):
            if goal == s[i: i + len(s)//2]:
                return True
        return False



# init sol
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) < 2:
            if s == goal:
                return True
            else:
                return False
        lst = [c for c in s]
        for i in range(len(goal)):
            if goal == "".join(lst):
                return True 
            # do shift here
            lstc = lst[:]
            for i in range(len(lst)):
                lst[i] = lstc[(i + 1) % len(lst)]
                
        return False