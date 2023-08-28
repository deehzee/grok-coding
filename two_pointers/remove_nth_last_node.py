"""
Given a singly linked list, remove the n-th node from the end of the list and
return its head.
"""

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def prepend_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = "LinkedList["
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += "]"
        return result

    __repr__ = __str__


def remove_nth_last_node(ll, n):
    assert n > 0, "n must be a positive integer"

    head = ll.head
    left = right = LinkedListNode(None, head)
    for i in range(n):
        if right and right.next:
            right = right.next
        else:
            return ll

    while right.next:
        left = left.next
        right = right.next

    if left.next == head:
        left.next = head.next
        head.next = None
        head = left.next
        left.next = None
    else:
        tmp = left.next
        left.next = tmp.next
        tmp.next = None

    ll.head = head
    return ll

