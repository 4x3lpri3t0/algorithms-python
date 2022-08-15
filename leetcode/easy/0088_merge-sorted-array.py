class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # NOTE: nums1 has a length of m + n (the last n elements are set to 0)
        p1 = 0
        p2 = 0
        while p2 < n:
            if nums1[p1] < nums2[p2]:
                p1 += 1  # leave it there
            else:
                # swap
                nums1[p1], nums2[p2] = nums2[p2], nums1[p1]
                p2 += 1
