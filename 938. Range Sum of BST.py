# Time Complexity: O(n)
# Space Complexity: O(n)

# Approach: Traverse the tree in pre-order fashion using a stack. If the current node's value is within the range, add it to the sum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # empty tree
        if root == None:
            return 0
        
        stack = []
        sum = 0

        stack.append(root)

        while len(stack) > 0:
            node = stack.pop()
            if node.val >= low and node.val <= high:
                sum += node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return sum