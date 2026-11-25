# 242. Valid Anagram
# Difficulty: Easy
# https://leetcode.com/problems/valid-anagram/
# Runtime: 29 ms | Memory: 14.2 MB

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_letters = [letter for letter in s]
        t_letters = [letter for letter in t]
        return sorted(s_letters) == sorted(t_letters)
