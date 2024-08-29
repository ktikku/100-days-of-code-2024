from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        char_map = defaultdict(int)
        for char in s1:
            char_map[char] += 1
        l = 0
        count = len(s1)
        for r in range(len(s2)):
            if char_map[s2[r]] > 0:
                count -= 1
            char_map[s2[r]] -= 1
            if count == 0:
                return True
            if r >= len(s1) - 1:
                if char_map[s2[l]] >= 0:
                    count += 1
                char_map[s2[l]] += 1
                l += 1
        return False