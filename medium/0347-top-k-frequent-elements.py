# 347. Top K Frequent Elements
# Difficulty: Medium
# https://leetcode.com/problems/top-k-frequent-elements/
# Runtime: 5 ms | Memory: 22.8 MB

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        ordered = sorted(frequency, key=lambda n: frequency[n], reverse=True)
        return ordered[:k]
