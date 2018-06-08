
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        
        ln = ListNode(None)
        start = 0
        Cur_Start = ln
        Cur = ln
        Cur1 = l1
        Cur2 = l2
        while True:
            if Cur1.val >= Cur2.val:
                if Cur2.next != None:
                    if start == 0:
                        Cur.val = Cur2.val
                        Cur2 = Cur2.next
                        start = 1
                    else:
                        Cur.next = Cur2
                        Cur2 = Cur2.next
                        Cur = Cur.next
                        Cur.next = None
                else:
                    if start == 0:
                        Cur.val = Cur2.val
                        Cur.next = Cur1
                        start = 1
                        break
                    else:
                        Cur.next = Cur2
                        Cur = Cur.next
                        Cur.next = Cur1
                        break
            else:
                if Cur1.next != None:
                    if start == 0:
                        Cur.val = Cur1.val
                        Cur1 = Cur1.next
                        start = 1
                    else:
                        Cur.next = Cur1
                        Cur1 = Cur1.next
                        Cur = Cur.next
                        Cur.next = None
                else:
                    if start == 0:
                        Cur.val = Cur1.val
                        Cur.next = Cur2
                        start = 1
                        break
                    else:
                        Cur.next = Cur1
                        Cur = Cur.next
                        Cur.next = Cur2
                        break
                        
        return Cur_Start 
        # Cur = Cur_Start
        # while Cur.next != None:
        #     print(Cur.val , '->')
        #     Cur = Cur.next
