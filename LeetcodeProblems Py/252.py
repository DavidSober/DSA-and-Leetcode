# here is a faster approach. we first sort the list by the first element 
# then we check the edges and make sure they are in the right order
# beats 60% in time and 44% in space
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True 

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