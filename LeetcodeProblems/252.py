# beats 5.7% in time and 30% in space
# brute force basically but it is ez

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        bounds = []
        for i in range(len(intervals)):
            for bound in bounds:
                if (intervals[i][0] <= bound[0] and intervals[i][1] <= bound[0]) or (intervals[i][0] >= bound[1] and intervals[i][1] >= bound[1]):
                    continue
                else:
                    return False
            bounds.append(intervals[i])
        return True