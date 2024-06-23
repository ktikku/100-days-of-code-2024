from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_dict = defaultdict(str)
        for i in range(len(t)):
            values = char_dict.values()
            if char_dict.get(s[i]) == None and t[i] not in values:
                char_dict[s[i]] = t[i]
            elif char_dict.get(s[i]) != t[i]:
                return False
            else:
                char_dict[s[i]] = t[i]
        return True
            