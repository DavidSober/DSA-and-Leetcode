# beats 23% in time and 7% in space

class SmallestInfiniteSet:

    def __init__(self):
        self.set = []
        for i in range(1, 1001): # first add all numbers 1,1000 inclusive to list
            self.set.append(i)
        heapq.heapify(self.set) # make it a heap so we can later access the smallest num in constant time 

    def popSmallest(self) -> int:
        return heapq.heappop(self.set)

    def addBack(self, num: int) -> None:
        if num in self.set:
            return
        else:
            heapq.heappush(self.set, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)