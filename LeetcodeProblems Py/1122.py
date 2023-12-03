# beats 5% in time LOL but 95% in space! not too bad 

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        missing = []
        for num in arr1:
            if num not in arr2:
                missing.append(num)
        arr1_new = []
        for i in range(len(arr2)):          # O(N^2) way of sorting arr1 according to order in arr2 (slow but works)
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    arr1_new.append(arr1[j])
        return arr1_new + sorted(missing)