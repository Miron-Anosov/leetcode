"""
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        cursor = 0
        len_ = len(nums)
        cursor_2 = 1
        if not nums:
            return []
        else:
            while True:
                if cursor + 1 == len_:
                    return []

                if (nums[cursor] + nums[cursor_2]) == target:
                    return [cursor, cursor_2]

                if cursor_2 + 1 < len_:
                    cursor_2 += 1
                else:
                    if cursor + 2 < len_:
                        cursor += 1
                    cursor_2 = cursor + 1


# O(n²)


s = Solution()


r1 = s.twoSum([2, 7, 11, 15], 9)
r2 = s.twoSum([3, 2, 4], 6)
r3 = s.twoSum([3, 3], 6)
r4 = s.twoSum([3, 2, 3], 6)

assert r1 == [0, 1], f"{r1} != [0, 1]"
assert r2 == [1, 2], f"{r2} != [1,2]"
assert r3 == [0,1], f"{r3} !=  [0, 1]"
assert r4 == [0, 2], f"{r4} !=  [0,2]"
