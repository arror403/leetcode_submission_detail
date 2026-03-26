class Solution:
    ##### power by chatGPT, modified #####
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next
        
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False
