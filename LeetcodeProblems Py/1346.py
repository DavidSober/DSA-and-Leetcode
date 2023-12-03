# beats 65% in time and 80% in space

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hset = set()
        for i in range(len(arr)):
            if arr[i] * 2 in hset or arr[i] / 2 in hset:
                return True
            hset.add(arr[i])
        return False