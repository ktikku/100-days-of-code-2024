# Time complexity: O(n)
# Space complexity: O(n)

# This is a simple problem, we can split the string by space and get the last element of the list and return the length of the last element.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        return len(a[-1])