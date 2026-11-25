# 217. Contains Duplicate
# Difficulty: Easy
# https://leetcode.com/problems/contains-duplicate/
# Runtime: 37 ms | Memory: 25.9 MB

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
