"""https://leetcode.com/problems/remove-element/"""


class Solution(object):
    def removeElement(self, nums: list, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        while index < len(nums):
            if nums[index] == val:
                nums.pop(index)
                index -= 1
            index += 1
        
        return len(nums)


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

x = Solution()
print(x.removeElement(nums, val))
