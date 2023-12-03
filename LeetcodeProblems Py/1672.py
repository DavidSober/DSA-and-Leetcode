# beats 53% in time and 96% in space lol ez 

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        temp = []
        for i in accounts:
            temp.append(sum(i))
        return max(temp)