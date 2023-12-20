class ListNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def removeDuplicates(head):
    slowPointer = head
    fastPointer = head

    while slowPointer:
        while fastPointer and fastPointer.data == slowPointer.data:
            fastPointer = fastPointer.next
        slowPointer.next = fastPointer
        slowPointer = fastPointer
    
    return head

l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(2)
l4 = ListNode(3)
l5 = ListNode(3)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5


print(removeDuplicates(l1))

while l1:
    print(l1.data)
    l1 = l1.next