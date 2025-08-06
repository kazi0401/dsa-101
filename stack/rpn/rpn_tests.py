import unittest
from rpn import eval_rpn

class TestEvaluateRPN(unittest.TestCase):

    def test_single_number(self):
        self.assertEqual(eval_rpn(["42"]), 42)

    def test_basic_addition(self):
        self.assertEqual(eval_rpn(["2", "3", "+"]), 5)

    def test_basic_subtraction(self):
        self.assertEqual(eval_rpn(["5", "2", "-"]), 3)

    def test_basic_multiplication(self):
        self.assertEqual(eval_rpn(["4", "3", "*"]), 12)

    def test_basic_division(self):
        self.assertEqual(eval_rpn(["10", "2", "/"]), 5)

    def test_multiple_operations(self):
        self.assertEqual(eval_rpn(["2", "1", "+", "3", "*"]), 9)  
        self.assertEqual(eval_rpn(["4", "13", "5", "/", "+"]), 6)  

    def test_negative_result(self):
        self.assertEqual(eval_rpn(["3", "4", "-"]), -1)

    def test_division_truncates_toward_zero(self):
        self.assertEqual(eval_rpn(["10", "3", "/"]), 3)
        self.assertEqual(eval_rpn(["-10", "3", "/"]), -3) 
        self.assertEqual(eval_rpn(["10", "-3", "/"]), -3)
        self.assertEqual(eval_rpn(["-10", "-3", "/"]), 3)

    def test_complex_expression(self):
        tokens = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
        self.assertEqual(eval_rpn(tokens), 14)


if __name__ == '__main__':
    unittest.main()

