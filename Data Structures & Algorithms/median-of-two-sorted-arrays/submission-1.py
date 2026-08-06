class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: #brute force solution
        nums1 += nums2 #extend the two lists together
        nums1.sort()

        n = len(nums1)
        med = n // 2

        if n % 2 == 1: #Odd number of elements in array
            return nums1[med]
        else: #even number of elements in array
            return float((nums1[med-1] + nums1[med]) / 2)