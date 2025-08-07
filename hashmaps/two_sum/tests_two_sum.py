import unittest

class TestTwoSum(unittest.TestCase):

    def setUp(self):
        from two_sum import two_sum
        self.two_sum = two_sum

    def test_basic_case(self):
        result = self.two_sum([2, 7, 11, 15], 9)
        self.assertEqual(set(result), set((0, 1)))

    def test_negative_numbers(self):
        result = self.two_sum([-1, -2, -3, -4], -6)
        self.assertEqual(set(result), set((1, 3)))

    def test_with_zero(self):
        result = self.two_sum([0, 4, 3, 0], 0)
        self.assertEqual(set(result), set((0, 3)))

    def test_duplicate_values(self):
        result = self.two_sum([3, 3], 6)
        self.assertEqual(set(result), set((0, 1)))

    def test_later_pair(self):
        result = self.two_sum([1, 2, 3, 4, 5], 9)
        self.assertEqual(set(result), set((3, 4)))

    def test_first_and_last(self):
        result = self.two_sum([5, 1, 2, 3, 4, 6], 11)
        self.assertEqual(set(result), set((0, 5)))

    def test_no_solution(self):
        result = self.two_sum([1, 2, 3], 10)
        self.assertIsNone(result)

    def test_single_element(self):
        result = self.two_sum([5], 5)
        self.assertIsNone(result)

    def test_empty_list(self):
        result = self.two_sum([], 5)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
