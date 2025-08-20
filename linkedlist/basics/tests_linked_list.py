
import unittest
from linked_list import *

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    # --------------------
    # Insertion tests
    # --------------------
    def test_insert_single(self):
        self.ll.insert(10)
        self.assertEqual(str(self.ll), "10 -> None")
        self.assertEqual(self.ll.length(), 1)

    def test_insert_multiple(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        self.assertEqual(str(self.ll), "3 -> 2 -> 1 -> None")
        self.assertEqual(self.ll.length(), 3)

    # --------------------
    # Search tests
    # --------------------
    def test_search_existing(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        self.assertEqual(self.ll.search(3), 0)  # head
        self.assertEqual(self.ll.search(2), 1)
        self.assertEqual(self.ll.search(1), 2)  # tail

    def test_search_non_existing(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.assertEqual(self.ll.search(99), -1)

    def test_search_empty_list(self):
        self.assertEqual(self.ll.search(1), -1)

    # --------------------
    # Deletion tests
    # --------------------
    def test_delete_middle(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)  # 3->2->1
        self.ll.delete(2)
        self.assertEqual(str(self.ll), "3 -> 1 -> None")
        self.assertEqual(self.ll.length(), 2)

    def test_delete_head(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)  # 3->2->1
        self.ll.delete(3)
        self.assertEqual(str(self.ll), "2 -> 1 -> None")
        self.assertEqual(self.ll.length(), 2)

    def test_delete_tail(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)  # 3->2->1
        self.ll.delete(1)
        self.assertEqual(str(self.ll), "3 -> 2 -> None")
        self.assertEqual(self.ll.length(), 2)

    def test_delete_non_existing(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.delete(99)  # Should not change the list
        self.assertEqual(str(self.ll), "2 -> 1 -> None")
        self.assertEqual(self.ll.length(), 2)

    def test_delete_from_empty(self):
        self.ll.delete(1)  # Should not crash
        self.assertEqual(str(self.ll), "None")
        self.assertEqual(self.ll.length(), 0)

    def test_delete_until_empty(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.delete(2)
        self.ll.delete(1)
        self.assertEqual(str(self.ll), "None")
        self.assertEqual(self.ll.length(), 0)

    # --------------------
    # Length tests
    # --------------------
    def test_length_empty(self):
        self.assertEqual(self.ll.length(), 0)

    def test_length_after_operations(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        self.assertEqual(self.ll.length(), 3)
        self.ll.delete(2)
        self.assertEqual(self.ll.length(), 2)
        self.ll.delete(3)
        self.assertEqual(self.ll.length(), 1)
        self.ll.delete(1)
        self.assertEqual(self.ll.length(), 0)


if __name__ == "__main__":
    unittest.main()
