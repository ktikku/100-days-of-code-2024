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

# Attempt 2:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        s = ''.join([char for char in s if char != ' ' and char.isalnum()]).lower()
        i = 0
        j = len(s) - 1
        print(s)
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True