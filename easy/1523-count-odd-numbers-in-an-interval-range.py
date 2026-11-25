# 1523. Count Odd Numbers in an Interval Range
# Difficulty: Easy
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
# Runtime: 13 ms | Memory: 12.2 MB

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return (high + 1) // 2 - low // 2
