# beats 13% in time and 14% in space

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        combos = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if i < j:
                    combos.append([arr[i]/arr[j], arr[i], arr[j]])
        lst = heapq.nsmallest(k, combos)[-1]
        numerator = lst[1]
        denominator = lst[2]
        return [numerator, denominator]
