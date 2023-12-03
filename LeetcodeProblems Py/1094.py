# beats 47% in time and 58% in space

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # idea from difference array from DSA course
        arr = [0] * (max(trips, key=lambda x: x[2])[2] + 1)
        for trip in trips:
            arr[trip[1]] += trip[0]
            arr[trip[2]] -= trip[0]
        pre = [arr[0]]
        for i in range(len(arr)):
            pre.append(pre[-1] + arr[i])
        return max(pre) <= capacity