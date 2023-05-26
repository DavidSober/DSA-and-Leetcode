# beats 51% in time and 35% in space
# NOTE BECAUSE THE PROBLEM SAYS THE INPUT IS ADDED FROM AN ORDERED INTEGER LIST we assume the input is sorted 
# THUS using the sortedlist and finding the median from that is valid and thus makes the probelm very trivial
# however I will leave the non sorted list assumption solution here since it is more useful if a problem in the
# future does not assume the input is sorted
class MedianFinder:

    def __init__(self):
        self.maxh = []
        self.minh = []

    def addNum(self, num: int) -> None:
        # you need to negate vals for max heap (the instructions did not say this key detail)
        # 1. Push num onto the max heap.
        # 2. Pop from the max heap, and push that onto the min heap.
        # 3. After step 2, if the min heap has more elements than the max heap, pop from the min heap and 
        # push the result onto the max heap.

        heapq.heappush(self.maxh, -num) # we need to negate in order to have a max heap
        mx = heapq.heappop(self.maxh)
        heapq.heappush(self.minh, -mx) # use abs when taking an element from max heap and inserting in min heap 
        if len(self.minh) > len(self.maxh):
            mn = heapq.heappop(self.minh) 
            heapq.heappush(self.maxh, -mn) # we need to re negate before pushing to max heap 
    def findMedian(self) -> float:
        if len(self.maxh) > len(self.minh):
            return -self.maxh[0]
        return (-self.maxh[0] + self.minh[0]) / 2 # always remember to negate something from max heap (annoying but needed)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()