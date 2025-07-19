class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index

        return []


nums_ = [2, 5, 1, 17]
d = Solution()
for i in 9, 7, 6, 19:
    print(d.twoSum(nums=nums_, target=i))