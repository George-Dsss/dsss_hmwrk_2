import unittest
from math_quiz import get_random_int, get_random_operator, generate_problem


class TestMathGame(unittest.TestCase):

    def test_get_random_int(self):
        # Test if random integer is within the specified range.
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        # Test if the operator is one of the specified choices.
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random choices
            operator = get_random_operator()
            self.assertIn(operator, operators)

    def test_generate_problem(self):
        # Test if math problem generation and answer calculation are correct.
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 3, '-', '7 - 3', 4),
            (4, 6, '*', '4 * 6', 24),
            (1, 0, '*', '1 * 0', 0)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
