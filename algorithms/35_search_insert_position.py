"""https://leetcode.com/problems/search-insert-position/description/"""

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104

"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return left


if __name__ == '__main__':
    sol = Solution()
    
    assert sol.searchInsert([1, 3, 5, 6], 5) == 2
    assert sol.searchInsert([1, 3, 5, 6], 2) == 1
    assert sol.searchInsert([1, 3, 5, 6], 7) == 4
    assert sol.searchInsert([1, 3, 5, 6, 14], 9) == 4
