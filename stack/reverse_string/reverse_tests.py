
from reverse_string import stack_reverse
import unittest


def create_case(array: list) -> tuple[list, list]:
    rev = array.copy()
    rev.reverse()

    return array, rev

class ReverseTest(unittest.TestCase):
        
    def test_basic(self):
        arr, rev = create_case([1, 2, 3])
        self.assertEqual(stack_reverse(arr), rev)

    def test_empty_list(self):
        arr, rev = create_case([])
        self.assertEqual(stack_reverse(arr), rev)

    def test_single_element(self):
        arr, rev = create_case([42])
        self.assertEqual(stack_reverse(arr), rev)

    def test_even_length(self):
        arr, rev = create_case([10, 20, 30, 40])
        self.assertEqual(stack_reverse(arr), rev)

    def test_odd_length(self):
        arr, rev = create_case([5, 15, 25, 35, 45])
        self.assertEqual(stack_reverse(arr), rev)

    def test_strings(self):
        arr, rev = create_case(["a", "b", "c"])
        self.assertEqual(stack_reverse(arr), rev)

    def test_nested_lists(self):
        arr, rev = create_case([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(stack_reverse(arr), rev)

    def test_mixed_types(self):
        arr, rev = create_case([1, "two", 3.0, [4]])
        self.assertEqual(stack_reverse(arr), rev)

    def test_original_unchanged(self):
        arr, _ = create_case([1, 2, 3])
        _ = stack_reverse(arr)
        self.assertEqual(arr, [1, 2, 3])




if __name__ == '__main__':
    unittest.main()