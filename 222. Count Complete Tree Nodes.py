# Time Complexity: O(n)
# Space Complexity: O(n)

# TODO: better solution with O(logn * logn) time complexity

# Approach:
# 1. We will use a stack to store the nodes.
# 2. We will start from the root and keep adding the nodes to the stack.
# 3. We will pop the node from the stack and increase count by one.
# 4. We will then add the right and left children of the node to the stack.
# 5. We will repeat the process until the stack is empty.
# 6. Finally, we will return the count.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        stack = []
        count = 0
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            count += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)        
        return count