import unittest
from tetris import simulate_tetris


class TestTetris(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"input": "Q0\n", "expected": "2\n"},
            {"input": "Z0\n", "expected": "2\n"},
            {"input": "S0\n", "expected": "2\n"},
            {"input": "T0\n", "expected": "2\n"},
            {"input": "I0\n", "expected": "1\n"},
            {"input": "L0\n", "expected": "3\n"},
            {"input": "J0\n", "expected": "3\n"},
            {"input": "I0,I4,Q8\n", "expected": "1\n"},
            {"input": "T1,Z3,I4\n", "expected": "4\n"},
            {"input": "Q0,I2,I6,I0,I6,I6,Q2,Q4\n", "expected": "3\n"},
            {"input": "I0\n", "expected": "1\n"},
            {"input": "Q0,Q2,Q4,Q6,Q8\n", "expected": "0\n"},
            {"input": "Q0,Q0,Q0,Q0,Q0\n", "expected": "10\n"},
            {"input": "T0,Z3,S5,I0,L8,I4\n", "expected": "5\n"},
            {"input": "I0,I1,I2,I3,I4,I5,I6\n", "expected": "7\n"},
            {"input": "I0,I0,I0,I0,I0\n", "expected": "5\n"},
            {"input": "I0,I4,Q8,Q0,I2,I6,I6,Q4\n", "expected": "3\n"},
            {"input": "L1,J1\n", "expected": "6\n"},
            {"input": "T1,Z3,S5,I4,L8,J6,T1,Z3,S5,I4,L8,J6\n", "expected": "14\n"},
        ]

    def test_tetris_cases(self):
        for test_case in self.test_cases:
            with self.subTest(test_case=test_case):
                input_data = test_case["input"].strip().split("\n")

                expected_output = test_case["expected"].strip()
                actual_output = "\n".join(simulate_tetris(input_data)).strip()

                self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
