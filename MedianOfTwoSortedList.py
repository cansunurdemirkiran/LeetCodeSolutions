class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
    
        merged_array = nums1 + nums2
        sorted_array = sorted(merged_array)
        len_array = len(sorted_array)

        if len_array % 2 == 1:
            #odd
            median_index = len_array // 2
            median_odd = sorted_array[median_index]
            return median_odd

        else:
            #even
            median_index = len_array // 2
            median_even = sorted_array[median_index - 1] + sorted_array[median_index]
            median_even = float(median_even) / 2
            return median_even
