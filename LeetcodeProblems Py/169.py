# beats 76% in time and 73% in space

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1cropped = []
        for i in range(0, m ):
            nums1cropped.append(nums1[i])
        addthis = sorted(nums1cropped + nums2)
        for i in range(len(nums1)):
            nums1[i] = addthis[i]
            