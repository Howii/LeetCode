# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    x = head
    head = x.next
    y = head.next

    head.next = x
    x.next = swapPairs(y)
    return head
