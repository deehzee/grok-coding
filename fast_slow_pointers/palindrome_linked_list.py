"""
Given the head of a linked list, your task is to check whether the linked list
is a palindrome or not. Return TRUE if the linked list is a palindrome;
otherwise, return FALSE.

"""

def is_palindrome(head):
    middle = find_middle(head)
    rev_mid = reverse(middle)
    p, q = head, rev_mid
    answer = True
    while q:
        if p.data != q.data:
            answer = False
            break
        p, q = p.next, q.next
    reverse(rev_mid)
    return answer


def reverse(head):
    prv, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prv
        prv, cur = cur, nxt
    return prv


def find_middle(head):
    """Find the middle of the linked list. Return the second node if even."""
    fast = slow = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow


def traverse(head):
    result = "LinkedList["
    cur = head
    while cur:
        result += str(cur.data)
        cur = cur.next
        if cur:
            result += ", "
    result += "]"
    return result


def create_linked_list(arr):
    ll = LinkedList()
    ll.create_linked_list(arr)
    return ll.head


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

