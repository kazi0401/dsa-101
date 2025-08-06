from stack import Stack, StackException
import unittest

class StackTester(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.elements = [1, 3, 4, 5, 1, 2]

        self.push_all(self.stack, self.elements)

    def push_all(stack: Stack, array: list) -> None:
        for elem in array:
            stack.push(elem)


    def test_push(self):
        self.assertEqual(self.elements, self.stack.data())

    def test_pop(self):
        self.stack.pop()
        self.assertEqual(self.elements[:-1], self.stack.data())
    
    def test_pop_nothing(self):
        stack = Stack()
        with self.assertRaises(StackException) as error: 
            stack.pop()
    
    def test_size(self):
        self.assertEqual(self.stack.size(), len(self.elements))
        self.stack.pop()
        self.assertEqual(self.stack.size(), len(self.elements) - 1)

    def test_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

        stack.push(1)
        self.assertFalse(stack.is_empty())






        




if __name__ == '__main__':
    unittest.main()






