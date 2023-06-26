# my original solution passed over 80% of test cases but
# big mistake was tieing ans to mid instead of left or right
# beats 54% in time and 11% in space

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # if len(dist) > hour: # edge case
        #     return -1
        if len(dist) > math.ceil(hour):
            return -1
        left = 1
        right = math.ceil(max(dist) * 100)
        def check(mid):
            tot = 0
            for i in range(len(dist) - 1):
                tot += math.ceil(dist[i] / mid)
            return tot + (dist[-1] / mid)
        while left <= right:
            mid = (left + right) // 2
            if check(mid) <= hour:
                right = mid - 1
            else:
                left = mid + 1
        return left