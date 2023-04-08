# beats 95% in time and 80% in space
def findMaxK(nums):
    test = sorted(nums, key=lambda x: abs(x), reverse=True) # sort by abs value in descending
# if the abs of both values are next to each other AND they are NOT both neg or both pos they are 
# a valid ans so we return since it is already reverse sorted
    for i in range(len(test) - 1):
        if abs(test[i]) == abs(test[i + 1]) and not (test[i] > 0 and test[i + 1] > 0) and not (test[i] < 0 and test[i + 1] < 0): 
            return abs(test[i]) # we will return in ans
    return -1 
