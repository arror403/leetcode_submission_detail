# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        cur = res

        while head:
            if head.val not in set(nums):
                cur.next = ListNode(head.val)
                cur = cur.next

            head = head.next


        return res.next