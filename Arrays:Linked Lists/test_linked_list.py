import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_push_and_pop(self):
        self.ll.push(1)
        self.ll.push(2)
        self.ll.push(3)
        self.assertEqual(self.ll.pop(), 3)
        self.assertEqual(self.ll.pop(), 2)
        self.assertEqual(self.ll.pop(), 1)
        with self.assertRaises(IndexError):
            self.ll.pop()

    def test_unshift_and_shift(self):
        self.ll.unshift(1)
        self.ll.unshift(2)
        self.ll.unshift(3)
        self.assertEqual(self.ll.shift(), 3)
        self.assertEqual(self.ll.shift(), 2)
        self.assertEqual(self.ll.shift(), 1)
        with self.assertRaises(IndexError):
            self.ll.shift()

    def test_getAt(self):
        self.ll.push(1)
        self.ll.push(2)
        self.ll.push(3)
        self.assertEqual(self.ll.getAt(0), 1)
        self.assertEqual(self.ll.getAt(1), 2)
        self.assertEqual(self.ll.getAt(2), 3)
        with self.assertRaises(IndexError):
            self.ll.getAt(3)

    def test_setAt(self):
        self.ll.push(1)
        self.ll.push(2)
        self.ll.push(3)
        self.ll.setAt(1, 20)
        self.assertEqual(self.ll.getAt(1), 20)
        with self.assertRaises(IndexError):
            self.ll.setAt(3, 30)

    def test_insertAt(self):
        self.ll.push(1)
        self.ll.push(2)
        self.ll.insertAt(1, 10)
        self.assertEqual(self.ll.getAt(1), 10)
        self.ll.insertAt(0, 0)
        self.assertEqual(self.ll.getAt(0), 0)
        with self.assertRaises(IndexError):
            self.ll.insertAt(5, 50)

    def test_removeAt(self):
        self.ll.push(1)
        self.ll.push(2)
        self.ll.push(3)
        self.ll.removeAt(1)
        self.assertEqual(self.ll.getAt(1), 3)
        self.ll.removeAt(0)
        self.assertEqual(self.ll.getAt(0), 3)
        with self.assertRaises(IndexError):
            self.ll.removeAt(2)

if __name__ == '__main__':
    unittest.main()
