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
        map_ = {}
        len_ = len(nums)
        for i in range((len_ // 2 if len_ % 2 == 0 else len_ // 2 + 1)):
            i2 = len_ - i - 1
            t1 = target - nums[i]
            t2 = target - nums[i2]

            if i != i2 and t1 + t2 == target:
                return [i, i2]

            i_map = map_.get(t1, map_.get(t2))

            if i_map is not None:
                if nums[i_map] + nums[i] == target:
                    return sorted((i_map, i))

                return sorted((i_map, i2))

            map_.update({nums[i]: i, nums[i2]: i2})

        return []


# O(n/2)
s = Solution()

r1 = s.twoSum([2, 7, 11, 15], 9)
r2 = s.twoSum([3, 2, 4], 6)
r3 = s.twoSum([3, 3], 6)
r4 = s.twoSum([3, 2, 3], 6)
r5 = s.twoSum([-3,4,3,90], 0)
r6 = s.twoSum([1,6142,8192,10239], 18431)
r7 = s.twoSum([2, 2, 1], 4)


assert r1 == [0, 1], f"{r1} != [0, 1]"
assert r2 == [1, 2], f"{r2} != [1,2]"
assert r3 == [0,1], f"{r3} !=  [0, 1]"
assert r4 == [0, 2], f"{r4} !=  [0,2]"
assert r5 == [0, 2], f"{r5} != [0, 2]"
assert r6 == [2, 3], f"{r6} != [2, 3]"
assert r7 == [0,1], f"{r7} != [0,1]"
