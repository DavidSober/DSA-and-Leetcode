# same as below but in one liner format 

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(list(set(arr1) & set(arr2) & set(arr3)))

# used bitwise and to get the elements in common much faster than with hashmap
# beats 94% in time and 20% in space

from sortedcontainers import SortedList
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        diff = set(arr1) & set(arr2) & set(arr3)
        return sorted(list(diff))

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