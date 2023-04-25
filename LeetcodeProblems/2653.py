from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        sl = SortedList()
        ret = []
        for i in range(k): # add the first k elements from nums to sortedlist. (aka set up first subarray)
            sl.add(nums[i])
        ret.append(min(0, sl[x-1])) # append either 0 if xth smallest element is non negative or xth smallest element if it is neg
        for i in range(k, len(nums)): # we start at k which means i represents the right index for the sliding window
            sl.add(nums[i])         # like with any sliding window first we add the rightmost element 
            sl.discard(nums[i-k])   # then we remove the leftmost element (to maintain window size k)
            ret.append(min(0, sl[x-1])) # (now we add the min of the curr window to ret)
        return ret