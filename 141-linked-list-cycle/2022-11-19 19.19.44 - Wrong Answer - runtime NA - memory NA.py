# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.detectLoop(head)

    def detectLoop(self, head):
        if (head == None):
            return False
        else:
            while (head != None):
                if (head.val == -1):
                    return True
                else:
                    head.val = -1
                    head = head.next
    
            return False