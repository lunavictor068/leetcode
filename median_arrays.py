'''
Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        median = 0
        added_length = len(nums1) + len(nums2)
        median_index = -(-added_length // 2)
        # even requires average of 2 medians
        if added_length % 2 == 0:
        	median_left, nums1_index, nums2_index = self.find_nth(median_index, nums1, nums2)
        	median_right, _, _ = self.find_nth(1, nums1, nums2, nums1_index, nums2_index)
        	median = (median_left + median_right) / 2
        # odd returns median
        else:
        	median, _, _ = self.find_nth(median_index, nums1, nums2)
        return median
        
    def find_nth(self, nth, nums1, nums2, nums1_index = 0, nums2_index=0):
        val = 0
        for _ in range(nth):
            if nums1_index > len(nums1) - 1:
                val = nums2[nums2_index]
                nums2_index += 1
            elif nums2_index > len(nums2) - 1:
                val = nums1[nums1_index]
                nums1_index += 1
            elif nums1[nums1_index] <= nums2[nums2_index]:
                val = nums1[nums1_index]
                nums1_index += 1
            else:
                val = nums2[nums2_index]
                nums2_index += 1
        return val, nums1_index, nums2_index

if __name__ == '__main__':
	n1 = [1,5,7,8,11,200,1000]
	n2 = [1,2,3,4,5]
	print(find_nth(1, n1, n2))
	print(find_nth(2, n1, n2))
	print(find_nth(3, n1, n2))
	print(find_nth(4, n1, n2))
	print(find_nth(5, n1, n2))
	print(find_nth(6, n1, n2))
	print(find_nth(7, n1, n2))
	print(find_nth(8, n1, n2))
	print(find_nth(9, n1, n2))
	print(find_nth(10, n1, n2))
	print(find_nth(11, n1, n2))
	print(find_nth(12, n1, n2))
	print("--- Median Test ---")
	nums1 = [1, 3]
	nums2 = [2]
	print(nums1, nums2)
	print(Solution.findMedianSortedArrays(Solution, nums1, nums2))