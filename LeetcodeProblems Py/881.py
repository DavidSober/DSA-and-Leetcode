# beats 28% in time and 18% in space

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            return 1
        ans = 0
        people.sort()
        people = deque(people)
        temp = 0
        while people:
            if people[0] + people[-1] > limit:
                people.pop()
                temp += 1
                continue
            people.popleft()
            if people:
                people.pop()
            ans += 1
        return ans + temp # ans is the number of pairs and temp is the number of individuals