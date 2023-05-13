# this is my second sol where i got rid of the for loop and sorting
# which should reduce it from O(nlogn) to just O(n)
# sure enough on paper this is a true improvement in time comp but time comp
# got worse somehow... leetcode is not consistent with these though
# beats 10% in time and 15% in space
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        lst = nums.copy()
        L = lst.index(max(lst))
        Lval = lst[L]
        lst.pop(L)
        L2 = lst.index(max(lst))
        L2val = lst[L2]
        if Lval/2 >= L2val:
            return L
        return -1
    
# here is the first sol 
# beats 15% in time and 15% in space
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        lst = nums.copy()
        ret = lst.index(max(lst))
        nums.sort(reverse=True)
        print(nums)
        L = nums[0]
        for i in range(1, len(nums)):
            if L == nums[i]:
                continue
            else:
                if L/2 >= nums[i]:
                    return ret
                else:
                    return -1