# Iterative Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach:
# 1. We will use a stack to store the nodes.
# 2. We will start from the root and keep adding the nodes to the stack.
# 3. We will pop the node from the stack and add its value to the result.
# 4. We will then add the right and left children of the node to the stack.
# 5. We will repeat the process until the stack is empty.
# 6. Finally, we will return the result.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        stack = []
        res = []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            res.append(node.val)
        return res
    

# Recursive Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach:
# 1. We will use a recursive function to traverse the tree.
# 2. We will add the value of the node to the result.
# 3. We will then call the function recursively on the left and right children of the node.
# 4. Finally, we will return the result.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return []
            return [node.val] + dfs(node.left) + dfs(node.right)
        return dfs(root)