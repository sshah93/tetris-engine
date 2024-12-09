
import unittest
from tetris_engine import TetrisEngine

class TestTetrisEngine(unittest.TestCase):
    def setUp(self):
        self.engine = TetrisEngine()

    def test_single_piece(self):
        result = self.engine.process_input_line("Q0")
        self.assertEqual(result, 2)

    def test_multiple_pieces(self):
        result = self.engine.process_input_line("I0,I4,Q8")
        self.assertEqual(result, 1)

    def test_no_row_clear(self):
        result = self.engine.process_input_line("T1,Z3,I4")
        self.assertEqual(result, 4)

    def test_complex_case(self):
        result = self.engine.process_input_line("Q0,I2,I6,I0,I6,I6,Q2,Q4")
        self.assertEqual(result, 3)

    def test_edge_case(self):
        result = self.engine.process_input_line("I0,I0,I0,I0")
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main()
