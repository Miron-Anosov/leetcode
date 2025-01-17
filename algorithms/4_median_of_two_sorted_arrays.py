"""https://leetcode.com/problems/median-of-two-sorted-arrays/description/"""
"""
4. Median of Two Sorted Arrays
Hard
Topics
Companies

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 
Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        median: float
        sorted_arrays = sorted(nums1)
        left, right = 0, len(nums1)
        mid = left + (right - left) // 2
        if right % 2 != 0:
            median = sorted_arrays[mid]
            return median
        median = (sorted_arrays[mid] + sorted_arrays[mid -1]) / 2
        return median


if __name__ == '__main__':
    solution = Solution()
    assert solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2]) == 2.0
    assert solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]) == 2.50
