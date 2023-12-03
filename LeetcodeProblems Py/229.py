# beats 7% in time and 14% in space
# perhaps we should try boor morres algo next?
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        F = len(nums)//3
        count = Counter(nums)
        ans = []
        for num in nums:
            if count[num] > F and num not in ans:
                ans.append(num)
        return ans