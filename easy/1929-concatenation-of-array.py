# 1929. Concatenation of Array
# Difficulty: Easy
# https://leetcode.com/problems/concatenation-of-array/
# Runtime: 2 ms | Memory: 19.4 MB

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = {}
        for i, num in enumerate(nums):
            ans[i] = num
        vals = [a for a in ans.values()]
        return vals + vals
