class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        s1 = set(nums1)
        s2 = set(nums2)
        if len(nums1) < len(nums2):
            for num in nums2:
                if num in s1:
                    return num
        for num in nums1:
            if num in s2:
                return num
        return -1