# beats 23% in time and 20% in spaec

from sortedcontainers import SortedList
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        F1, F2, F3 = Counter(arr1), Counter(arr2), Counter(arr3)
        Ftot = F1 + F2 + F3
        sl = SortedList()
        for key in Ftot:
            if Ftot[key] == 3:
                sl.add(key)
        return list(sl)