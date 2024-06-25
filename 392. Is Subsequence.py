# This is a two pointer solution. We keep two pointers i and j. i is the pointer for the string s and 
# j is the pointer for the string t. We iterate through the string t and if we find a match we increment 
# both i and j. If we don't find a match we increment j. If we reach the end of s we return True else 
# we return False.

# Time complexity: O(n)
# Space complexity: O(1)
# Two Pointer Solution

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:   
        i, j = 0, 0
        if len(s) == 0:
            return True
        while (j < len(t) and i < len(s)):
            if s[i] is not None and s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == len(s):
            return True
        return False                     
        