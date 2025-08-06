import unittest
from stack_problems import is_balanced


class TestBalancedParentheses(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_balanced(""))

    def test_single_pair(self):
        self.assertTrue(is_balanced("()"))
        self.assertTrue(is_balanced("[]"))
        self.assertTrue(is_balanced("{}"))

    def test_nested_pairs(self):
        self.assertTrue(is_balanced("([])"))
        self.assertTrue(is_balanced("{[()]}"))
        self.assertTrue(is_balanced("[({})]"))

    def test_multiple_pairs(self):
        self.assertTrue(is_balanced("()[]{}"))
        self.assertTrue(is_balanced("([]){}"))
        self.assertTrue(is_balanced("()[{}([])]"))

    def test_unbalanced_missing_closing(self):
        self.assertFalse(is_balanced("("))
        self.assertFalse(is_balanced("[["))
        self.assertFalse(is_balanced("{[("))

    def test_unbalanced_missing_opening(self):
        self.assertFalse(is_balanced(")"))
        self.assertFalse(is_balanced("]]"))
        self.assertFalse(is_balanced("})"))

    def test_wrong_order(self):
        self.assertFalse(is_balanced("(]"))
        self.assertFalse(is_balanced("[)"))
        self.assertFalse(is_balanced("{]"))
        self.assertFalse(is_balanced("[(])"))

    def test_mixed_valid_and_invalid(self):
        self.assertFalse(is_balanced("()[(]){}"))
        self.assertFalse(is_balanced("([]{})("))
        self.assertFalse(is_balanced("[(])()"))

if __name__ == '__main__':
    unittest.main()