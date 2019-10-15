"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        node = ListNode(value, next=self.head)
        if self.head != None:
            self.head.prev = node
        self.head = node
        self.length += 1
        if len(self) == 1:
            self.tail = self.head

    def remove_from_head(self):
        if len(self) == 0:
            return None
        elif len(self) == 1:
            value = self.head.value
            del self.tail
            del self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        next = self.head.next
        value = self.head.value
        next.prev = None
        del self.head
        self.head = next
        self.length -= 1
        return value

    def add_to_tail(self, value):
        node = ListNode(value, self.tail)
        if self.tail != None:
            self.tail.next = node
        self.tail = node
        self.length += 1
        if len(self) == 1:
            self.head = self.tail

    def remove_from_tail(self):
        if len(self) == 0:
            return None
        elif len(self) == 1:
            value = self.tail.value
            del self.tail
            del self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        prev = self.tail.prev
        value = self.tail.value
        prev.next = None
        del self.tail
        self.tail = prev
        self.length -= 1
        return value

    def move_to_front(self, node):
        if len(self) < 2 or node == self.head:
            return
        if len(self) == 2 and node == self.tail:
            self.head, self.tail = self.tail, self.head
            self.head.next = self.head.prev
            self.tail.prev = self.tail.next
            return
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.head.prev = node
        node.prev = None
        node.next = self.head
        self.head = node

    def move_to_end(self, node):
        if len(self) < 2 or node == self.tail:
            return
        if len(self) == 2 and node == self.head:
            self.head, self.tail = self.tail, self.head
            self.head.next = self.head.prev
            self.tail.prev = self.tail.next
            return
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.tail.next = node
        node.next = None
        node.prev = self.tail
        self.tail = node

    def delete(self, node):
        if node == None:
            return None
        if len(self) == 1:
            node.delete()
            self.head = None
            self.tail = None
            self.length -= 1
            return
        if len(self) == 2:
            node.delete()
            self.length -= 1
            if node == self.head:
                self.head = self.tail
                self.tail.prev = None
            else:
                self.tail = self.head
                self.head.next = None
            return
        if node == self.head:
            next_node = node.next
            self.head = next_node
        elif node == self.tail:
            prev_node = node.prev
            self.tail = prev_node
        node.delete()
        self.length -= 1

    def get_max(self):
        node = self.head
        llmax = -inf
        while node != None:
            if node.value > llmax:
                llmax = node.value
            node = node.next
        return llmax