class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        if not nums: return None

        lens = len(nums)
        if lens == 1: return nums[0]

        middle = lens / 2

        if lens % 2 == 0:
            return (nums[middle-1] + nums[middle]) / 2.0
        else:
            return float(nums[middle])
