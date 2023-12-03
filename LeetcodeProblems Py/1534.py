# brute forece seems to be the only solution... unless you use a Fenwick Tree
# which requires knowing fenwick tree and bucket sort very well, come back when you
# know those two topics better
# beats 5% in time and 86% in space

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(len(arr) - 2):
            for j in range(len(arr) - 1):
                for k in range(len(arr)):
                    good_A = abs(arr[i] - arr[j]) <= a
                    good_B = abs(arr[j] - arr[k]) <= b
                    good_C = abs(arr[i] - arr[k]) <= c
                    if good_A and good_B and good_C and i < j and j < k:
                        ans += 1
        return ans