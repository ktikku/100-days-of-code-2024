# Time Complexity: O(n)
# Space Complexity: O(n)

#Approach: We maintain a stack to keep track of the current directory. If we encounter a './' we continue, 
# if we encounter a '../' we pop from the stack if it is not empty. Otherwise we continue. 
# If we encounter a directory name, we append it to the stack. Finally we return the length of the stack.

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == './':
                continue
            elif log == '../':
                if len(stack) > 0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(log)
        return len(stack)