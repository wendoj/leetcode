# 125. Valid Palindrome
# Difficulty: Easy
# https://leetcode.com/problems/valid-palindrome/
# Runtime: 11 ms | Memory: 19.6 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalised = ''
        for char in s:
            lower = char.lower()
            if lower.isalnum():
                normalised += lower
        return normalised == normalised[::-1]
