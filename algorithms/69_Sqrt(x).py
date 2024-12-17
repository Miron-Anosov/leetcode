"""https://leetcode.com/problems/sqrtx/description/"""
"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

 

Constraints:

    0 <= x <= 231 - 1


"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while right >= left:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif x < mid * mid:
                right = mid - 1
            else:
                left = mid + 1

        return right


sol = Solution()

try:
    assert sol.mySqrt(x=0) == 0
    assert sol.mySqrt(x=4) == 2
    assert sol.mySqrt(x=8) == 2
    assert sol.mySqrt(x=25) == 5
    assert sol.mySqrt(x=49) == 7
    assert sol.mySqrt(x=50) == 7
    assert sol.mySqrt(x=72) == 8
    assert sol.mySqrt(x=-72) == 8
except AttributeError as e:
    print(e)
