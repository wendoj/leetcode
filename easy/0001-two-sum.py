# 1. Two Sum
# Difficulty: Easy
# https://leetcode.com/problems/two-sum/
# Runtime: 0 ms | Memory: 13.1 MB

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
