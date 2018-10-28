# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        
        head_node = ListNode(-1)
        current_node = head_node
        before_node = None
        upper_one = 0
        
        while l1 and l2:
            current_node.next = ListNode(-1)
            val_sum = l1.val + l2.val + upper_one
            if val_sum >= 10:
                val_sum -= 10
                upper_one = 1
            else:
                upper_one = 0
            current_node.val = val_sum
            before_node = current_node
            current_node = current_node.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            current_node.next = ListNode(-1)
            val_sum = l1.val + upper_one
            if val_sum>=10:
                val_sum -= 10
                upper_one = 1
            else:
                upper_one = 0
            current_node.val = val_sum
            before_node = current_node
            current_node = current_node.next
            l1 = l1.next
        
        while l2:
            current_node.next = ListNode(-1)
            val_sum = l2.val + upper_one
            if val_sum>=10:
                val_sum -= 10
                upper_one = 1
            else:
                upper_one = 0
            current_node.val = val_sum
            before_node = current_node
            current_node = current_node.next
            l2 = l2.next
            
        if upper_one==1:
            current_node.val = 1
        else:
            before_node.next = None
            
        return head_node     
                