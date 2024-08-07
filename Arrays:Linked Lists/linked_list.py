from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        new_node = Node(val)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self.length += 1

    def unshift(self, val):
        new_node = Node(val)
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
        current = self.head
        while current.next != self.tail:
            current = current.next
        value = self.tail.value
        self.tail = current
        self.tail.next = None
        self.length -= 1
        return value

    def shift(self):
        if not self.head:
            raise IndexError("Shift from empty list")
        value = self.head.value
        self.head = self.head.next
        if not self.head:
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
        new_node = Node(val)
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        new_node.next = current.next
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
        self.length -= 1
        return value
