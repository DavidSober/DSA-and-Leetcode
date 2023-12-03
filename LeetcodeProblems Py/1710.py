# beats 5% in time and 47% in space

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        while truckSize:
            if not boxTypes:
                break
            ans += boxTypes[0][1]
            boxTypes[0][0] -= 1
            truckSize -= 1
            if boxTypes[0][0] == 0:
                boxTypes.pop(0) # use deque later
        return ans