# here is my heap solution.
# this is much better than the first two solutions.
# While it is true that a sortedlist is ez and maybe in an interview I would do it at first
# Heap ensures the best time and space comp and it can be scaled to internet of things size 
# data which is pretty cool
# beats 27% in time and 41% in space
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val) # first push new val to heap
        while len(self.nums) != self.k: # we want a min heap of size k since that will ensure that 
            heapq.heappop(self.nums)  # we have O(1) time to access the kth largest element 
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# here is my fastest solution i used sortedlist object in this so 
# it may or may not be acceptable for an interview 
# beats 13% in time and 6% in space

from sortedcontainers import SortedList

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = SortedList(nums, key=lambda x: -x)

    def add(self, val: int) -> int:
        self.nums.add(val)
        return self.nums[self.k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# here is my first sol
# beats 5% in time 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)