# one liner 
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum( abs(x - y) for x, y in zip(sorted(seats), sorted(students)) )
    

# first sol did it in 1:30 
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        for x, y in zip(seats, students):
            ans += abs(x - y)
        return ans