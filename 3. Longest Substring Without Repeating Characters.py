# Time Complexity: O(n)
# Space Complexity: O(min(n, m)) where n is the length of the string and m is the size of the character set
# Approach: Use a sliding window to keep track of the longest substring without repeating characters.
# 1. Initialize a set to keep track of the characters in the current window.
# 2. Initialize two pointers l and r to keep track of the start and end of the window.
# 3. Iterate over the string and keep adding characters to the set.
# 4. If the character is already present in the set, remove the character at the start of the window and increment l.
# 5. Update the result with the maximum length of the window.
# 6. Return the result.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            result = max(result, r - l + 1)

        return result        