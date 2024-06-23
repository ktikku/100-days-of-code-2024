# Time complexity: O(n)
# Space complexity: O(n)
# Hash Map Solution

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            group[key].append(strs[i])
        return group.values()
