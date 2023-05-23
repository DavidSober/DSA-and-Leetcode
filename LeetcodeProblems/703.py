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