# beats 50% in time and 20% in space

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        sl = sorted(nums1 + nums2, key=lambda x: x[0])
        new = []
        i = 0
        while i < len(sl) - 1:
            if sl[i][0] == sl[i + 1][0]:
                new.append([sl[i][0], sl[i][1] + sl[i + 1][1]])
                i += 2
            else:
                new.append([sl[i][0], sl[i][1]])
                i += 1
        if new[-1][0] == sl[-1][0]:
            return new
        else:
            return new + [sl[-1]]