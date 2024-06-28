# Time Complexity: O(n)
# Space Complexity: O(n)

"""
Iterate over the path string, keeping track of the current directory name. 
Use a stack to keep track of the directories. If the current directory name is '..', 
pop the last directory from the stack. If the current directory name is not empty and not '.', 
add it to the stack. Finally, join the directories in the stack with '/' and return the result.
"""

"""
Adding an extra slash at the end ensures that the loop processes the last directory or file name in the path. 
Without the extra slash, the loop might not recognize the end of the last directory or file name, 
especially if the path doesn't already end with a slash. This technique simplifies parsing the path 
by treating the end of each directory or file name uniformly, facilitating operations like splitting 
the path into components.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        curr = ''
        stack = []
        for char in path + '/':
            if char == '/':
                if curr == '..':
                    if stack:
                        stack.pop()
                elif curr != '' and curr != '.':
                    stack.append(curr)
                curr = ''
            else:
                curr += char
        return '/' + '/'.join(stack)