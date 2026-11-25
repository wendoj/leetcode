# 20. Valid Parentheses
# Difficulty: Easy
# https://leetcode.com/problems/valid-parentheses/
# Runtime: 4 ms | Memory: 12.4 MB

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        corresponding_brackets = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        brackets = []

        for char in s:
            if char in corresponding_brackets:
                brackets.append(char)
            else:
                if not brackets or corresponding_brackets[brackets.pop()] != char:
                    return False
        return not brackets
