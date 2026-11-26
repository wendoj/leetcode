# 49. Group Anagrams
# Difficulty: Medium
# https://leetcode.com/problems/group-anagrams/
# Runtime: 21 ms | Memory: 15.9 MB

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())
