## Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def add(l1, l2, carry):
            if l1 is None and l2 is None and carry == 0:
                return
            
            res = carry
            l1_next = None
            l2_next = None
            
            if l1:
                l1_next = l1.next
                res += l1.val 
            if l2:
                l2_next = l2.next
                res += l2.val

            carry = res // 10
            res = res % 10

            node = ListNode()
            node.val = res
            node.next = add(l1_next, l2_next, carry)

            return node

        return add(l1, l2, 0)
            

                