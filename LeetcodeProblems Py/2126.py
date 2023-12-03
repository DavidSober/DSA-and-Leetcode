# beats 6% in time and 93% in space
# this is a greedy

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        heapq.heapify(asteroids)
        while len(asteroids) > 0:
            ast = heapq.heappop(asteroids)
            if mass >= ast:
                mass += ast
            else:
                return False
        return True