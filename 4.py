# 4. Median of Two Sorted Arrays

import math

"""
Since I only need the coordinates at the center of the merged array—for odd-sized (m+n)/2 and for 
even-sized (m+n)/2 ± 0.5—I iterate through both arrays until the floor((m+n) / 2) coordinate, storing
the last two positions, and avoiding processing the other half of the merged array. I return their 
average for even (curr+prev)/2 and the last position for odd (curr).
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        curr = None
        prev = None
        center = (m+n)/2
        i = 0
        j = 0
        while True:
            # print(i, j, i+j, center)
            if i+j > math.floor(center):
                break
            condition1 = False
            condition2 = False
            if i < m:
                num_1_number = nums1[i]
                condition1 = True
            if j < n:
                num_2_number = nums2[j]
                condition2 = True
            
            # print(num_1_number, num_2_number)
            if condition1 and condition2:
                if num_1_number < num_2_number:
                    prev = curr
                    curr = num_1_number
                    i = i+1
                else:
                    prev = curr
                    curr = num_2_number
                    j = j+1
            elif condition1:
                prev = curr
                curr = num_1_number
                i = i+1
            elif condition2:
                prev = curr
                curr = num_2_number
                j = j+1
            else:
                break
        # print(prev, curr)
        if (m+n) % 2 == 0:
            median = (prev+curr)/2
        else:
            median = curr
        return median