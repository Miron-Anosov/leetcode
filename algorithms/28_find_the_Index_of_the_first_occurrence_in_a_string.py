"""https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


haystack_1 = "sadbutsad"
needle_1 = "sad"
haystack_2 = "leetcode"
needle_2 = "leeto"
haystack_3 = "mississippi"
needle_3 = "issip"

x = Solution()

assert x.strStr(haystack=haystack_1, needle=needle_1) == 0
assert x.strStr(haystack=haystack_2, needle=needle_2) == -1
assert x.strStr(haystack=haystack_3, needle=needle_3) == 4
