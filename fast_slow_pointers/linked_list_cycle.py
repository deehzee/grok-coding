"""
Check whether or not a linked list contains a cycle. If a cycle exists, return
TRUE. Otherwise, return FALSE.  The cycle means that at least one node can be
reached again by traversing the `NEXT` pointer.

"""

def detect_cycle(head):
    if not head or not head.next:
        return False
    slow, fast = head, head.next
    while fast and slow != fast:
        slow = slow.next
        if fast.next:
            fast = fast.next.next
        else:
            break
    return slow == fast


def detect_cycle2(head):
    if not head:
        return False
    fast, slow = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            return True
    return False


# Template for linked list node class
class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Template for the linked list
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
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    # returns the number of nodes in the linked list
    def get_length(self, head):
        temp = head
        length = 0
        while(temp):
            length+=1
            temp = temp.next
        return length

    # returns the node at the specified position(index) of the linked list
    def get_node(self, head, pos):
        if pos != -1:
            p = 0
            ptr = head
            while p < pos:
                ptr = ptr.next
                p += 1
            return ptr

    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result

    __repr__ = __str__


