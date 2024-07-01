# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Use a stack to keep track of the depth of the parenthesis.

class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
                count = max(count, len(stack))
                print(count)
            if len(stack) > 0:
                top = len(stack) - 1
                if stack[top] == '(' and char == ')':
                    stack.pop()
        return count
        