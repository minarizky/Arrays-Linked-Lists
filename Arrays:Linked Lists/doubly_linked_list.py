from node import Node

class DoublyNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        new_node = DoublyNode(val)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self.length += 1

    def unshift(self, val):
        new_node = DoublyNode(val)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self.length += 1

    def pop(self):
        if not self.head:
            raise IndexError("Pop from empty list")
        if self.head == self.tail:
            value = self.head.value
            self.head = self.tail = None
            self.length -= 1
            return value
        value = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        return value

    def shift(self):
        if not self.head:
            raise IndexError("Shift from empty list")
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.length -= 1
        return value

    def getAt(self, idx):
        if idx < 0 or idx >= self.length:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def setAt(self, idx, val):
        if idx < 0 or idx >= self.length:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(idx):
            current = current.next
        current.value = val

    def insertAt(self, idx, val):
        if idx < 0 or idx > self.length:
            raise IndexError("Index out of bounds")
        if idx == 0:
            self.unshift(val)
            return
        if idx == self.length:
            self.push(val)
            return
        new_node = DoublyNode(val)
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        self.length += 1

    def removeAt(self, idx):
        if idx < 0 or idx >= self.length:
            raise IndexError("Index out of bounds")
        if idx == 0:
            return self.shift()
        if idx == self.length - 1:
            return self.pop()
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        value = current.next.value
        current.next = current.next.next
        current.next.prev = current
        self.length -= 1
        return value
