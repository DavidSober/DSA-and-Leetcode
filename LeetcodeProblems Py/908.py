class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:


        def isEven(num):
            if num % 2 == 0:
                return True
            else:
                return False
        evens = []
        odds = []
        for i in range(len(nums)):

            if isEven(nums[i]):
                evens.append(nums[i])
            else:
                odds.append(nums[i])

        return evens + odds
        