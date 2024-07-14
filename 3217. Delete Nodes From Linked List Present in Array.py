# Time Complexity: O(n)
# Space Complexity: O(n)

# Approach:
# 1. We will first convert the nums to a set.
# 2. We will then iterate through the linked list and check if the value is present in the set.
# 3. If the value is present in the set, we will skip the node.
# 4. If the value is not present in the set, we will move to the next node.
# 5. Finally, we will return the head of the linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        head = res = ListNode(-1, head)

        while head.next:
            if head.next.val in nums:
                head.next = head.next.next
            else:
                head = head.next

        return res.next