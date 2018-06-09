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
        return self.deathadder(0, l1, l2)
        
    def deathadder(self, prev, l1, l2):
        now_val = (l1.val+l2.val+prev)%10
        next_add = (l1.val+l2.val+prev)//10
        NP = ListNode(now_val)
        if l2.next != None and l1.next != None:
            NP.next = self.deathadder(next_add, l1.next, l2.next)
        elif l2.next != None:
            NP.next = self.deathadder(next_add, ListNode(0), l2.next)
        elif l1.next != None:
            NP.next = self.deathadder(next_add, l1.next, ListNode(0))
        else:
            if next_add != 0:
                NP.next = ListNode(next_add)
            else:
                NP.next = None
        return NP
    
            
            
