# beats 84% in time and 93% in space

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        F = Counter(arr)
        temp = sorted(F.values(), reverse=True)
        for i in range(k):
            temp[-1] -= 1
            if temp[-1] == 0:
                temp.pop()
        return len(temp)
