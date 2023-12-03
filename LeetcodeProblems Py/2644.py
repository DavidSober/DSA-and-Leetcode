# beats 11% in time and 94% in space

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        
        maxI = 0
        maxN = 0
        for i in range(len(divisors)):
            count = 0
            for j in range(len(nums)):
                if nums[j] % divisors[i] == 0:
                    count += 1
    # If there is more than one integer with the maximum score, return the minimum of them.
            if count == maxN and divisors[maxI] > divisors[i]:
                maxI = i
                maxN = max(maxN, count)
                #print(i, maxI)
            if count > maxN:
                maxN = max(maxN, count)
                maxI = i
        return divisors[maxI]