# Time complexity: O(n)
# Space complexity: O(n)
# Hash Map Solution

from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        match_map = defaultdict(str)
        words = s.split()
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            values = match_map.values()
            if match_map.get(pattern[i]) == None and words[i] not in values:
                match_map[pattern[i]] = words[i]
            elif match_map.get(pattern[i]) != words[i]:
                return False
            else:
                match_map[pattern[i]] = words[i]
        return True
    