# uses the idea of difference array 
# beats 5% in time and 5% in space

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        arr = [0] * (max(intervals, key=lambda x: x[1])[1] + 1)
        for interval in intervals:
            arr[interval[0]] += 1
            arr[interval[1]] -= 1
        pre = [arr[0]]
        for i in range(1, len(arr)):
            pre.append(pre[-1] + arr[i])
        return max(pre)