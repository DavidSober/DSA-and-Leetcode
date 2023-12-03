# beats 12.8% in time and 24% in space

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 4:
            if target in nums:
                return nums.index(target)
            else:
                return -1
        left = 0
        right = len(nums) - 1
        pivot = None
        while left <= right:
            mid = (left + right) // 2
            if nums[mid + 1] < nums[mid]:
                pivot = mid
                break
            if nums[mid] > nums[right]:
                left = mid + 1
                if nums[left + 1] < nums[left]:
                    pivot = left
            else:
                right = mid - 1
                if nums[right + 1] < nums[right]:
                    pivot = right
        if pivot != None:
            R1 = bisect.bisect_left(nums, target, 0, pivot)
            if not 0 <= R1 <= len(nums) - 1:
                return -1
            if nums[R1] == target:
                return R1
            R2 = bisect.bisect_left(nums, target, pivot + 1, len(nums) - 1)
            if not 0 <= R2 <= len(nums) - 1:
                return -1
            if nums[R2] == target:
                return R2
            else: 
                return -1
        else:
            pot = bisect.bisect_left(nums, target)
            if nums[pot] == target:
                return pot
            else: 
                return -1 
        return -1 