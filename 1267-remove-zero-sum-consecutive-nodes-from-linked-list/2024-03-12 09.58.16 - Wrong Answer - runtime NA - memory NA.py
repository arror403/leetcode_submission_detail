# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=self.remove_consecutive_zero_sum_sequences(self.LinkedToArr(head))
        return self.ArrToLinked(t)


    def remove_consecutive_zero_sum_sequences(self, lst):
        """
        Removes all consecutive sequences that sum to zero from the given list.
        
        Args:
            lst (list): The input list of numbers.
        
        Returns:
            list: A new list with all consecutive zero-sum sequences removed.
        """
        result = []
        current_sum = 0
        start_index = 0
        
        for i in range(len(lst)):
            current_sum += lst[i]
            
            while current_sum != 0 and start_index < i:
                current_sum -= lst[start_index]
                start_index += 1
            
            if current_sum == 0:
                start_index = i + 1
            else:
                result.append(lst[i])
        
        return result


    def ArrToLinked(self, l):
        cur = dummy = ListNode(0)
        for n in l:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next
        
        
    def LinkedToArr(self, head):
        arr = []
        curr = head
        while (curr != None): 
            arr.append(curr.val)
            curr = curr.next
        return arr