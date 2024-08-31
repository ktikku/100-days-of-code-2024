from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_count = 0
        max_length = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])
            # If the current window size minus the count of the most frequent character is greater than k,
            # it means we need to shrink the window from the left
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
