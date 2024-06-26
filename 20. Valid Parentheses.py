# Time Complexity: O(n)
# Space Complexity: O(n)
# Stack Solution

# This is a stack solution. We iterate through the string and if we find an opening bracket we push it onto the stack.
# If we find a closing bracket we check if the stack is empty or if the top of the stack is the corresponding opening bracket.
# If it is we pop the opening bracket from the stack. If we reach the end of the string we check if the stack is empty. If it is
# we return True else we return False.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            elif char == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif char == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        return len(stack) == 0
        