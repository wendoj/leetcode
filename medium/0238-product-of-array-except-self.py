# 238. Product of Array Except Self
# Difficulty: Medium
# https://leetcode.com/problems/product-of-array-except-self/
# Runtime: 36 ms | Memory: 27.6 MB

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = [1] * n 
        right = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        return [left[i] * right[i] for i in range(n)]
