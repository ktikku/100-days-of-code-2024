class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_string = ''.join(e for e in s if e.isalnum())
        formatted_string = formatted_string.lower()
        mid = len(formatted_string)/2
        l, r = 0, len(formatted_string) - 1
        print(formatted_string)
        while l < mid:
            if formatted_string[l] != formatted_string[r]:
                return False
            l += 1
            r -= 1
        return True