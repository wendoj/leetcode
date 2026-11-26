# 347. Top K Frequent Elements
# Difficulty: Medium
# https://leetcode.com/problems/top-k-frequent-elements/
# Runtime: 7 ms | Memory: 13.8 MB

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        ordered = sorted(frequency, key=lambda n: frequency[n], reverse=True)
        return ordered[:k]
