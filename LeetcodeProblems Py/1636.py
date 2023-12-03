from collections import Counter
def frequencySort(nums):
    count = Counter(nums)
    return sorted(nums, key = lambda x: (count[x], -x)) 


nums = [-1,1,-6,4,5,-6,1,4,1]
frequencySort(nums) 