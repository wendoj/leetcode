# 242. Valid Anagram
# Difficulty: Easy
# https://leetcode.com/problems/valid-anagram/
# Runtime: 27 ms | Memory: 13.2 MB

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
