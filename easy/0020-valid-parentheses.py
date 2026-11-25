# 20. Valid Parentheses
# Difficulty: Easy
# https://leetcode.com/problems/valid-parentheses/
# Runtime: 3 ms | Memory: 12.2 MB

class Solution(object):
    def isValid(self, s):
        pairs = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            elif not stack or stack.pop() != char:
                return False
        return not stack
