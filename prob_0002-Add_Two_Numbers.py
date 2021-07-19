# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = 0
    dummyHead = cur = ListNode(0)
    while l1 or l2 or carry:
        v1 = 0 if l1 is None else l1.val
        v2 = 0 if l2 is None else l2.val
        w = v1 + v2 + carry
        if w > 9:
            w -= 10
            carry = 1
        else:
            carry = 0
        cur.next = ListNode(w)
        cur = cur.next
        l1 = None if l1 is None else l1.next
        l2 = None if l2 is None else l2.next

    return dummyHead.next
