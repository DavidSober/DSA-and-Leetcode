# using a max heap we can do this problem much faster
# beats 69% in time and 5% in space
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        thresh = sum(nums) / 2
        ans = 0 
        curr_sum = sum(nums)
        nums = [-num for num in nums] # negate the list to create max heap
        heap = heapq.heapify(nums) # created heap
        while curr_sum > thresh:
            mx = abs(heapq.heappop(nums)) / 2
            heapq.heappush(nums, -mx) # we have to re negate the element before pushing back to the negated heap
            curr_sum -= mx
            ans += 1
        return ans

# beats 5% in time and 5% in space
# we can use a heap to do better but this is a decent first try

from sortedcontainers import SortedList
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        thresh = sum(nums) / 2
        ans = 0
        sl = SortedList(nums)
        curr_sum = sum(sl)
        while curr_sum > thresh:
            mx = sl[-1] / 2 # to be added
            del sl[-1]
            sl.add(mx)
            curr_sum -= mx
            ans += 1
        return ans