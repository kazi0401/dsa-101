import unittest

class TestCountFrequencies(unittest.TestCase):

    def setUp(self):
        from frequency_counter import frequency_counter
        self.frequency_counter = frequency_counter

    def test_empty_list(self):
        self.assertEqual(self.frequency_counter([]), {})

    def test_single_element(self):
        self.assertEqual(self.frequency_counter(["a"]), {"a": 1})

    def test_multiple_elements(self):
        self.assertEqual(
            self.frequency_counter(["a", "b", "a", "c", "b", "a"]),
            {"a": 3, "b": 2, "c": 1}
        )

    def test_with_numbers(self):
        self.assertEqual(
            self.frequency_counter([1, 2, 2, 3, 1, 1]),
            {1: 3, 2: 2, 3: 1}
        )

    def test_with_mixed_types(self):
        self.assertEqual(
            self.frequency_counter(["x", 1, "x", 1, True, False, True]),
            {"x": 2, 1: 2, True: 2, False: 1}
        )

    def test_case_sensitivity(self):
        self.assertEqual(
            self.frequency_counter(["A", "a", "A"]),
            {"A": 2, "a": 1}
        )


if __name__ == '__main__':
    unittest.main()