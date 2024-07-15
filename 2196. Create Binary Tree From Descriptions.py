# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Create a dictionary to store the nodes and a set to store the children.
#           Iterate over the descriptions and create the nodes and connect them.
#           Return the node that is not in the children set.
#           This is the root of the tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children_set = set()

        for parent, child, is_left in descriptions:
            children_set.add(child)
            # create new nodes
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            # connect nodes
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        
        for parent, child, is_left in descriptions:
            if parent not in children_set:
                return nodes[parent]
            