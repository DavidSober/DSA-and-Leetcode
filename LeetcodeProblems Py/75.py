# did bubble sort here. O(n^2) time and O(1) space. find a faster sort algo later

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True


# beats 6% in time and 7% in space since this is a selection sort (not optimal)
# at a later date add a more optimaal sorting method

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        for i in range(len(nums)):
            min_index = i
            for j in range(i + 1, len(nums)):
                # Update minimum index
                if nums[j] < nums[min_index]:
                    min_index = j

            # Swap current index with minimum element in rest of list
            nums[min_index], nums[i] = nums[i], nums[min_index]